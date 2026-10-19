


import sys
from pathlib import Path

# Add the Loom project root to Python's module search path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import transformers.dynamic_module_utils as dmu

_original_get_imports = dmu.get_imports


def get_imports_without_flash_attn(filename):
    imports = _original_get_imports(filename)

    if filename.endswith("modeling_florence2.py"):
        imports = [name for name in imports if name != "flash_attn"]

    return imports


dmu.get_imports = get_imports_without_flash_attn

import uvicorn
from space.app import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
