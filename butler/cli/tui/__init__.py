import os.path
import time

from rich.live import Live
from rich.tree import Tree


class FileTreeUI:
    def __init__(self, root: str):
        if not root:
            raise Exception("root can't be null")

        self.root = root
        self.root_node = Tree(self.root)
        self.nodes = {os.path.abspath(self.root): self.root_node}

        self.live = Live(auto_refresh=True, refresh_per_second=10)

    def add(self, abs_path: str, file: str):
        abs_path = os.path.abspath(abs_path)
        parent_node = self.__get_parent_node(abs_path)
        if parent_node is self.root_node and abs_path != self.root:
            parent_node = self.root_node.add(abs_path[len(self.root) + 1 :])
            self.nodes[abs_path] = parent_node
        parent_node.add(file)

    def __get_parent_node(self, path: str) -> Tree:
        if path in self.nodes:
            return self.nodes.get(path)
        else:
            return self.__get_parent_node(os.path.abspath(os.path.join(path, "../..")))

    def update(self):
        self.live.update(self.root_node)
        time.sleep(0.4)
