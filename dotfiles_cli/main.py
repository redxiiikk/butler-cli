import typer

from dotfiles_cli.cli import dotfile

app: typer.Typer = typer.Typer()

app.add_typer(dotfile.app, name="dotfile")
