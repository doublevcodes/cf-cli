import runpy

import typer
from pathlib import Path

APP_NAME = "Cloudflare CLI"
app = typer.Typer()

commands_path = Path(__file__).parent.resolve() / "command_groups"

for file in commands_path.iterdir():
    module = runpy.run_path(file)[file.stem]
    app.add_typer(module, name=file.stem)


__all__ = (
    "app"
)