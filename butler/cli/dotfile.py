import os

import typer

from butler.service.dotfile import DotfileService
from butler.utils import EchoUtils

app: typer.Typer = typer.Typer()


@app.callback(invoke_without_command=True)
def update(
    ctx: typer.Context, dotfiles_repo: str = typer.Argument(None, help="dotfile repo config, just support local repo")
):
    if ctx.invoked_subcommand is not None:
        return

    if not dotfiles_repo:
        EchoUtils.error("dotfile repo can't none")
        raise typer.Exit(code=1)

    if not os.path.isabs(dotfiles_repo):
        dotfiles_repo = os.path.join(os.getcwd(), dotfiles_repo)

    if not os.path.exists(dotfiles_repo) or not os.path.isdir(dotfiles_repo):
        EchoUtils.error(f"config repo path not existed: {dotfiles_repo}")
        return typer.Exit(1)

    EchoUtils.info("start update dotfile")
    for root, parent, dotfile in DotfileService.update(dotfiles_repo):
        EchoUtils.debug(f"TUI Tree: {root} - {parent} - {dotfile}")


if __name__ == "__main__":
    app()
