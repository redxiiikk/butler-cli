import typer

from butler.cli import dotfile
from butler.utils import EchoUtils

app: typer.Typer = typer.Typer()

app.add_typer(dotfile.app, name="dotfile")


@app.callback(invoke_without_command=True)
def butler(ctx: typer.Context):
    if ctx.invoked_subcommand is not None:
        return

    EchoUtils.debug("butler...")
