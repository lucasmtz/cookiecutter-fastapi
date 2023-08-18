#!/bin/sh

update_config() {
    local file=$1
    shift
    for line in "$@"; do
        grep -qxF "$line" "$file" || echo "$line" >> "$file"
    done
}

# --- Python build dependencies ---

printf "\nInstalling Python build dependencies...\n"
sudo apt-get update -y
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# --- PyEnv ---

if [ -x "$(command -v pyenv)" ]; then
    printf "\nPyEnv is already installed. Updating...\n"
    pyenv update
else
    printf "\nPyEnv is not installed. Installing...\n"
    curl https://pyenv.run | bash
fi   
printf "\nSetting up your shell environment for Pyenv...\n"
pyenv_setup_lines=(
    'export PYENV_ROOT="$HOME/.pyenv"'
    'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"'
    'eval "$(pyenv init -)"'
)
update_config ~/.bashrc "${pyenv_setup_lines[@]}"
update_config ~/.profile "${pyenv_setup_lines[@]}"
update_config ~/.bash_profile "${pyenv_setup_lines[@]}"


# --- Poetry ---

printf "\nUninstalling Poetry if installed using the deprecated get-poetry.py script...\n"
rm -rf "${POETRY_HOME:-~/.poetry}"
export PATH=$(echo $PATH | sed -e 's#'"$HOME"'/.poetry/bin##g; s/::*/:/g; s/^://; s/:$//')

if [ -x "$(command -v poetry)" ]; then
    printf "\nPoetry is already installed. Uninstalling to avoid locked version self-update error...\n"
    curl -sSL https://install.python-poetry.org | python3 - --uninstall
fi
printf "\nInstalling Poetry...\n"
curl -sSL https://install.python-poetry.org | python3 -

printf "\nSetting up your shell environment for Poetry...\n"
poetry_setup_lines=(
    'export PATH="$HOME/.local/bin:$PATH"'
)
update_config ~/.bashrc "${poetry_setup_lines[@]}"
update_config ~/.profile "${poetry_setup_lines[@]}"
update_config ~/.bash_profile "${poetry_setup_lines[@]}"

# Enable tab completion for Bash
poetry completions bash >>~/.bash_completion

printf "\nConfiguring Poetry...\n"
poetry config virtualenvs.in-project true
poetry config virtualenvs.prefer-active-python true

