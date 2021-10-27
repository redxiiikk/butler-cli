import typer


def info(text: str):
    typer.echo(typer.style(text, fg="blue"))


def error(text: str):
    typer.echo(typer.style(text, fg="red"))


def debug(text: str):
    typer.echo(typer.style(text, fg="white"))
