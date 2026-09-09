"""GPU preflight and unchanged pilot, within the same Slurm step/process."""
import hashlib
import os
from pathlib import Path
import runpy
import socket
import subprocess
import sys

root = Path(__file__).resolve().parent
print('STAGE 1: environment', flush=True)
print('Host:', socket.gethostname(), 'Python:', sys.executable, flush=True)
print('CUDA_VISIBLE_DEVICES:', os.environ.get('CUDA_VISIBLE_DEVICES'), flush=True)
print('PYTHONPATH:', os.environ.get('PYTHONPATH'), flush=True)
for name in ('pilot.py', 'recovery_run.py', 'model_lock.json'):
    print(name, hashlib.sha256((root / name).read_bytes()).hexdigest(), flush=True)
subprocess.run(['nvidia-smi'], check=False)
import torch
import transformers
print('Torch:', torch.__version__, torch.__file__, flush=True)
print('Transformers:', transformers.__version__, transformers.__file__, flush=True)
print('CUDA build:', torch.version.cuda, 'Built architectures:', torch.cuda.get_arch_list(), flush=True)
if torch.__version__ != '2.6.0+cu118':
    raise RuntimeError('Wrong torch environment; rerun recovery_setup.sh.')
print('STAGE 2: CUDA initialization and arithmetic', flush=True)
torch.cuda.init()
print('GPU:', torch.cuda.get_device_name(0), 'Capability:', torch.cuda.get_device_capability(0), flush=True)
with torch.inference_mode():
    a = torch.ones((32, 32), dtype=torch.float16, device='cuda')
    assert torch.allclose(a @ a, torch.full_like(a, 32))
    left = torch.ones((1, 32, 1), dtype=torch.float32, device='cuda')
    right = torch.ones((1, 1, 4), dtype=torch.float32, device='cuda')
    assert torch.allclose(left @ right, torch.ones((1, 32, 4), device='cuda'))
torch.cuda.synchronize()
del a, left, right
torch.cuda.empty_cache()
print('GPU PREFLIGHT OK. STAGE 3: model loading and pilot evaluation', flush=True)
sys.argv = [str(root / 'pilot.py'), 'run', *sys.argv[1:]]
runpy.run_path(str(root / 'pilot.py'), run_name='__main__')
