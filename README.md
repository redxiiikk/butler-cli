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

[![PreRelease Build](https://github.com/redxiiikk/butler-cli/actions/workflows/pre-release-build.yml/badge.svg)](https://github.com/redxiiikk/butler-cli/actions/workflows/pre-release-build.yml)


Butler 是一个你最忠诚的管家，帮助你更好的管理、使用自己的电脑。
它可以做到很多的事情，例如可以帮助你在多台电脑间同步你的配置、软件、插件等等。

## 🔨 安装

> 暂时只能从源码进行编译，后续将提供安装脚本

```shell
$ git clone https://github.com/redxiiikk/butler-cli.git
$ cd butler-cli
$ go build -o butler
```

## ✨ Features

- [x] 同步 dotfiles

## 🚀 如何使用

### 管理本地 dotfile

```shell
$ ./butler dotfile --help
Sync your dotfile

Usage:
  butler dotfile [flags]

Flags:
  -h, --help   help for dotfile

$ ./butler dotfile ../dotfile-repo
CREATE:     /home/user/.gitconfig -> /home/user/dotfile-repo/gitconfig
CREATE:     /home/user/.gitconfig -> /home/user/dotfile-repo/gitconfig
CREATE:         /home/user/.zshrc -> /home/user/dotfile-repo/zshrc
```

## ✅ Todo

- [ ] GitHub Actions 打包
- [ ] GitHub 依赖版本监测
- [ ] 本地配置文件支持
- [ ] 添加安装脚本
- [ ] 单元测试覆盖
- [ ] 添加 dotfile 文件
