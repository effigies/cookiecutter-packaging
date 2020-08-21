from pathlib import Path

if __name__ == "__main__":
    if '{{ cookiecutter.use_pyproject }}':
        Path("pyproject.toml").unlink()
