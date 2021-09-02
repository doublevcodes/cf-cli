from pathlib import Path

import typer

from cf.cli import app


if __name__ == "__main__":
    APP_NAME = "Cloudflare CLI"
    app_dir = Path(typer.get_app_dir(APP_NAME))
    app_dir.mkdir(exist_ok=True)
    cache = Path(app_dir / ".cache.json")
    cache.touch(exist_ok=True)
    app()