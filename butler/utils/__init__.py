import os.path
import platform
import typing as t

import typer


class EchoUtils:
    @staticmethod
    def info(text: str):
        typer.echo(typer.style(text, fg="blue"))

    @staticmethod
    def error(text: str):
        typer.echo(typer.style(text, fg="red"))

    @staticmethod
    def debug(text: str):
        typer.echo(typer.style(text, fg="white"))


class DirectoryUtils:
    @staticmethod
    def walk(
        root: str,
        parent: str = None,
        filter_func: t.Callable[[str, str, str], bool] = None,
    ):
        parent = parent if parent else ""
        directory = os.path.join(root, parent)

        if not os.path.isdir(directory):
            EchoUtils.error(f"this isn't a directory: {directory}")
            return

        for sub in os.listdir(directory):
            if filter_func and not filter_func(root, parent, sub):
                continue

            if os.path.isdir(os.path.join(directory, sub)):
                yield from DirectoryUtils.walk(root, os.path.join(parent, sub), filter_func)
            elif os.path.isfile(os.path.join(directory, sub)):
                yield root, parent, sub
            else:
                EchoUtils.error(f"unknown type: {directory}")


class FileUtils:
    @staticmethod
    def is_hidden_file(file: str) -> bool:
        if platform.system() == "Windows":
            pass
        else:
            return os.path.basename(file).startswith(".")
