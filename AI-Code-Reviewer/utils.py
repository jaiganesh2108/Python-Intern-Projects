import subprocess
import tempfile
import os

def run_flake8(code: str) -> str:
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp:
        tmp.write(code.encode())
        tmp_path = tmp.name

    result = subprocess.run(["flake8", tmp_path], capture_output=True, text=True)
    os.unlink(tmp_path)
    return result.stdout or "No linting issues found."

def run_black(code: str) -> str:
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp:
        tmp.write(code.encode())
        tmp_path = tmp.name

    subprocess.run(["black", tmp_path, "--quiet"])
    with open(tmp_path, "r") as f:
        formatted_code = f.read()
    os.unlink(tmp_path)
    return formatted_code

def run_radon(code: str) -> str:
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp:
        tmp.write(code.encode())
        tmp_path = tmp.name

    result = subprocess.run(["radon", "cc", tmp_path, "-s"], capture_output=True, text=True)
    os.unlink(tmp_path)
    return result.stdout or "No complexity issues found."
