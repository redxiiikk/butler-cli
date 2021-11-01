import os.path
import typing as t

from butler.utils import DirectoryUtils, EchoUtils, FileUtils


class DotfileService:
    HOME = f"{os.getenv('HOME')}"

    @classmethod
    def update(cls, dotfiles_repo: str):
        if not os.path.exists(dotfiles_repo):
            EchoUtils.error(f"dotfiles repo not existed: {dotfiles_repo}")
            return

        for root, parent, dotfile in DirectoryUtils.walk(
            dotfiles_repo,
            filter_func=DotfileService.__filter_hidden_file,
        ):
            if not cls.__do_update_dotfile(root, parent, dotfile):
                EchoUtils.debug("error!")
                return

            yield root, parent, dotfile

    @classmethod
    def __do_update_dotfile(cls, root: str, parent: t.Optional[str], dotfile: str) -> bool:
        parent = parent if parent else ""

        symlink = os.path.abspath(f"{cls.HOME}/.{parent}/{dotfile}" if parent else f"{cls.HOME}/.{dotfile}")
        dotfile = os.path.abspath(os.path.join(root, parent, dotfile))

        if not os.path.exists(dotfile) or not os.path.isfile(dotfile):
            EchoUtils.error(f"dotfile not existed or isn't a file: {dotfile}")
            return False

        if not os.path.exists(symlink):
            os.symlink(dotfile, symlink)
            return True

        if os.path.isdir(symlink):
            EchoUtils.error(f"symlink is a directory: {symlink}")
            return False

        if os.path.isfile(symlink):
            os.remove(symlink)
            os.symlink(dotfile, symlink)

        if os.path.islink(symlink) and os.path.realpath(symlink) != dotfile:
            os.unlink(symlink)
            os.symlink(dotfile, symlink)

        return True

    @staticmethod
    def __filter_hidden_file(root: str, parent: t.Optional[str], file: str) -> bool:
        parent = parent if parent else ""
        return not FileUtils.is_hidden_file(os.path.join(root, parent, file))
