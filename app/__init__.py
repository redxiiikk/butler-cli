import typer

from app.cli import dotfile

app: typer.Typer = typer.Typer()

app.add_typer(dotfile.app, name="dotfile")
