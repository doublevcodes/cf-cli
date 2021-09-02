import typer
from textwrap import dedent
from pathlib import Path
import orjson

from cf.backend.endpoints.token import verify


user = typer.Typer()

@user.command("login")
def user_login():
    access_token = typer.prompt(typer.style("Input thy access token which beholds the permissions thee grants Cloudflare CLI 🌍 ", fg="blue"), hide_input=True)
    confirm = typer.confirm(typer.style(f"Are thee willin' to proceed with this here token: {typer.style(f'{access_token[:8]}...', fg='red')} ✅ ", fg="green"))
    if confirm:
        typer.secho(f"Making useth of access token {typer.style(f'{access_token[:8]}...', fg='red')} 😁 ", fg="yellow")
        cache = Path(typer.get_app_dir("Cloudflare CLI")) / ".cache.json"
        with open(cache, 'r') as cache_file:
            if cache_file.read() != "":
                cache_file.seek(0)
                cache_content = orjson.loads(cache_file.read())
            else:
                cache_content = {}
        if not cache_content.get("token", False):
            if verify(access_token)['success']:
                with open(cache, 'wb') as cache_file:
                    cache_content['token'] = access_token
                    cache_file.write(orjson.dumps(dict(cache_content)))
                typer.secho(f"Successfully did check thy token {typer.style(f'{access_token[:8]}...', fg='red')} ✅ ", fg="green")
                typer.secho("Cloudflare CLI bids thee farewell 👋 ", fg="bright_yellow")
            else:
                typer.secho(f"Thy token ({f'{access_token[:8]}...'}) seemeth not to be valid 🚫 ", fg="red")
                raise typer.Exit()
        else:
            tok = cache_content["token"]
            replace = typer.confirm(typer.style(
                f"Wouldst thee liketh to replaceth thy existing token ("
                f"{typer.style(f'{tok[:8]}...', fg='red')}) with "
                f"token {typer.style(f'{access_token[:8]}...', fg='red')}? 🔍 ",
                fg="green"))
            if replace:
                if verify(access_token)['success']:
                    with open(cache, 'wb') as cache_file:
                        cache_content['token'] = access_token
                        cache_file.write(orjson.dumps(dict(cache_content)))
                    typer.secho(f"Successfully did check thy token {typer.style(f'{access_token[:8]}...', fg='red')} ✅ ", fg="green")
                    typer.secho("Cloudflare CLI bids thee farewell 👋 ", fg="bright_yellow")
                else:
                    typer.secho(f"Thy token ({f'{access_token[:8]}...'}) seemeth not to be valid 🚫 ", fg="red")
                    raise typer.Exit()
            else:
                typer.secho("Haply anoth'r day 👋 ", fg="orange")
                raise typer.Exit()
    else:
        typer.secho("Haply anoth'r day 👋 ", fg="bright_yellow")
        raise typer.Exit()