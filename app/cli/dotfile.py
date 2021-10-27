import os

import typer

from app.utils import echo

app: typer.Typer = typer.Typer()



def hanle_dotfile_symlink(repo_file: str, symlink_file: str):
    repo_file = os.path.abspath(repo_file)
    symlink_file = os.path.abspath(symlink_file)

    if not os.path.exists(symlink_file):
        echo.debug(f"{repo_file}:{symlink_file}")
        return
    
    if not os.path.islink(symlink_file):
        echo.debug(f"{repo_file}:{symlink_file}")
        return
    
    if os.path.realpath(symlink_file) != repo_file:
        echo.debug(f"this is a symlink file: {repo_file}:{os.path.realpath(symlink_file)}")
        return
    
    echo.debug(f"don't need update dotfile: {symlink_file}")
    return


def walk_dotfile(root: str, parent: str = None):
    for sub_file in os.listdir(f"{root}/{parent}" if parent else root):
        # don't handle hidden file in linux and mac
        if sub_file.startswith("."):
            continue

        sub_file_path = (
            f"{root}/{parent}/{sub_file}" if parent else f"{root}/{sub_file}"
        )

        if os.path.isdir(sub_file_path):
            walk_dotfile(
                root, f"{parent}/{sub_file}" if parent else sub_file
            )
        elif os.path.isfile(sub_file_path):
            hanle_dotfile_symlink(
                f"{root}/{parent}/{sub_file}" if parent else f"{root}/{sub_file}",
                f"{os.getenv('HOME')}/.{parent}/{sub_file}" if parent else f"{os.getenv('HOME')}/.{sub_file}"
            )
        else:
            echo.error(f"unknown file type: {sub_file_path}")


@app.command()
def update(
    dotfiles_repo_path: str = typer.Argument(
        None, help="dotfile repo config, just support local repo"
    )
):
    if not os.path.isabs(dotfiles_repo_path):
        dotfiles_repo_path = os.path.join(os.getcwd(), dotfiles_repo_path)

    if not os.path.exists(dotfiles_repo_path) or not os.path.isdir(dotfiles_repo_path):
        echo.error(f"config repo path not existed: {dotfiles_repo_path}")
        return typer.Exit(1)

    if not os.path.isdir(dotfiles_repo_path):
        echo.error(f"config repo is not a directory: {dotfiles_repo_path}")
        return typer.Exit(1)

    echo.info("start update dotfile")
    walk_dotfile(dotfiles_repo_path)


@app.command()
def add():
    typer.echo("zsh")


if __name__ == "__main__":
    app()
