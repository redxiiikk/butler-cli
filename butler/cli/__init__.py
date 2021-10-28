import typer

from butler.cli import dotfile

app: typer.Typer = typer.Typer()

app.add_typer(dotfile.app, name="dotfile")
