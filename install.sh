if [ "$(uname)" == "Darwin" ]; then
    PRE_RELEASE_DOWNLOAD_URL="https://github.com/redxiiikk/butler-cli/releases/download/prerelease/butler-darwin"
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    PRE_RELEASE_DOWNLOAD_URL="https://github.com/redxiiikk/butler-cli/releases/download/prerelease/butler-linux"
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    echo "not support windows!!!"
    exit 1
fi

if [ ! -d "$HOME/.butler/bin" ]; then
    mkdir -p "$HOME/.butler/bin"
fi

curl -L "$PRE_RELEASE_DOWNLOAD_URL" -o "$HOME/.butler/bin/butler"
chmod u+x "$HOME/.butler/bin/butler"

if [ -f "$HOME/.zshrc" ]; then
    SHELL_CONFIG_FILE="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
    SHELL_CONFIG_FILE="$HOME/.bashrc"
else
    ehco "can't find shell config file!!!"
    exit 1
fi

if [ "$(cat $SHELL_CONFIG_FILE | grep 'PATH="$HOME/.butler/bin:$PATH"' | wc -l)" -lt 1 ]; then
    echo 'PATH="$HOME/.butler/bin:$PATH"' >> "$SHELL_CONFIG_FILE"
    echo
    echo "添加 shell 配置"
fi

echo
echo "Installation is complete, Please run:"
echo "    source $SHELL_CONFIG_FILE"