import os.path
import typing as t

import typer

from butler.utils import DirectoryUtils, EchoUtils, FileUtils


class Dotfile:
    HOME = f"{os.getenv('HOME')}"

    def __init__(self, root: str, parent: t.Optional[str], dotfile: str):
        if parent is None:
            parent = ""

        self.dotfile_path = os.path.abspath(os.path.join(root, parent, dotfile))

        if not os.path.exists(self.dotfile_path) and not os.path.isfile(self.dotfile_path):
            raise typer.Exit(code=1)

        self.symlink_path = os.path.abspath(f"{self.HOME}/.{parent}/{dotfile}" if parent else f"{self.HOME}/.{dotfile}")

    def create_symlinks(self):
        if not os.path.exists(self.symlink_path):
            os.symlink(self.dotfile_path, self.symlink_path)

        if os.path.isdir(self.symlink_path):
            EchoUtils.error(f"symlink is a directory: {self.symlink_path}")
            return

        if os.path.isfile(self.symlink_path):
            os.remove(self.symlink_path)
            os.symlink(self.dotfile_path, self.symlink_path)

        if os.path.islink(self.symlink_path) and os.path.realpath(self.symlink_path) != self.dotfile_path:
            os.unlink(self.symlink_path)
            os.symlink(self.dotfile_path, self.symlink_path)

    @property
    def status(self) -> bool:
        return os.path.realpath(self.symlink_path) == self.dotfile_path


class DotfileService:
    HOME = f"{os.getenv('HOME')}"

    @classmethod
    def update(cls, dotfiles_repo: str):
        for root, parent, dotfile in DirectoryUtils.walk(
            dotfiles_repo,
            filter_func=DotfileService.__is_hidden_file,
        ):
            if not cls.__do_update_dotfile(Dotfile(root, parent, dotfile)):
                EchoUtils.debug("error!")
                return

            yield root, parent, dotfile

    @classmethod
    def __do_update_dotfile(cls, dotfile: Dotfile) -> bool:
        dotfile.create_symlinks()
        return dotfile.status

    @staticmethod
    def __is_hidden_file(root: str, parent: t.Optional[str], file: str) -> bool:
        parent = parent if parent else ""
        return not FileUtils.is_hidden_file(os.path.join(root, parent, file))
