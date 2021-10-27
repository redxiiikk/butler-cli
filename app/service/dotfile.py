import os.path
import typing as t

from app.utils import EchoUtils, DirectoryUtils, FileUtils


class DotfileService:
    HOME = f"{os.getenv('HOME')}"

    @classmethod
    def update(cls, dotfiles_repo: str):
        if not os.path.exists(dotfiles_repo):
            EchoUtils.error(f"dotfiles repo not existed: {dotfiles_repo}")
            return

        DirectoryUtils.walk(
            dotfiles_repo,
            handle_func=DotfileService.__do_update_dotfile,
            filter_func=DotfileService.__filter_hidden_file,
        )

    @classmethod
    def __do_update_dotfile(cls, root: str, parent: t.Optional[str], dotfile: str):
        parent = parent if parent else ""

        symlink = os.path.abspath(
            f"{cls.HOME}/.{parent}/{dotfile}" if parent else f"{cls.HOME}/.{dotfile}"
        )
        dotfile = os.path.abspath(os.path.join(root, parent, dotfile))

        if not os.path.exists(symlink):
            EchoUtils.debug(f"{dotfile}:{symlink}")
            return

        if not os.path.islink(symlink):
            EchoUtils.debug(f"{dotfile}:{symlink}")
            return

        if os.path.realpath(symlink) != dotfile:
            EchoUtils.debug(
                f"this is a symlink file: {dotfile}:{os.path.realpath(symlink)}"
            )
            return

        EchoUtils.debug(f"don't need update dotfile: {symlink}")
        return

    @staticmethod
    def __filter_hidden_file(root: str, parent: t.Optional[str], file: str) -> bool:
        parent = parent if parent else ""
        return not FileUtils.is_hidden_file(os.path.join(root, parent, file))
