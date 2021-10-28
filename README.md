<pre align="center">
 ▄▄▄▄    █    ██  ██▓    ▄▄▄█████▓▓█████  ██▀███  
▓█████▄  ██  ▓██▒▓██▒    ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▓██  ▒██░▒██░    ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
▒██░█▀  ▓▓█  ░██░▒██░    ░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
░▓█  ▀█▓▒▒█████▓ ░██████▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
░▒▓███▀▒░▒▓▒ ▒ ▒ ░ ▒░▓  ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
▒░▒   ░ ░░▒░ ░ ░ ░ ░ ▒  ░    ░     ░ ░  ░  ░▒ ░ ▒░
 ░    ░  ░░░ ░ ░   ░ ░     ░         ░     ░░   ░ 
 ░         ░         ░  ░            ░  ░   ░     
      ░                                           
</pre>

Butler 是一个你最忠诚的管家，帮助你更好的管理、使用自己的电脑。
它可以做到很多的事情，例如可以帮助你在多台电脑间同步你的配置、软件、插件等等。

## 🔨 安装

```shell
$ git clone https://github.com/redxiiikk/butler-cli.git
$ cd butler-cli
$ poetry install
$ peotry build
$ pip install --user dist/butler-<version>-py3-none-any.whl # please replace the version number
```

> 参考文档: [Build a Package - Typer](https://typer.tiangolo.com/tutorial/package/#create-a-wheel-package)

## ✨ Features

- [x] 同步 dotfiles

## 🚀 如何使用

```shell
$ butler --help
Usage: butler [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  dotfile

$ butler dotfile --help
Usage: butler dotfile [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  update

$ butler dotfile update --help 
Usage: butler dotfile update [OPTIONS] [DOTFILES_REPO]

Arguments:
  [DOTFILES_REPO]  dotfile repo config, just support local repo

Options:
  --help  Show this message and exit.

$ update ../dotfiles 
start update dotfile
create dotfile symlink: : /home/user/dotfiles/docker/config.json:/home/user/.docker/config.json
create dotfile symlink: : /home/user/dotfiles/docker/daemon.json:/home/user/.docker/daemon.json
create dotfile symlink: : /home/user/dotfiles/gitconfig:/home/user/.gitconfig
create dotfile symlink: : /home/user/dotfiles/gitignore:/home/user/.gitignore
create dotfile symlink: : /home/user/dotfiles/zshrc:/home/user/.zshrc
```

## ✅ Todo

- [ ] 同步 oh my zsh 插件
- [ ] 同步软件
- [ ] 完善文档工作
- [ ] 配置化支持
- [ ] 设置定时任务
- [ ] 支持 Github 仓库