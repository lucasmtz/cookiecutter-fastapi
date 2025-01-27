#!/bin/sh

# -----------------------------------------------------------------------------------------------------------------
# Install Python build dependencies - PyEnv builds Python from source so you need to install all the build dependencies
# -----------------------------------------------------------------------------------------------------------------
printf "\nInstalling Python build dependencies...\n"
sudo apt-get update -y
sudo apt install -y build-essential gcc libssl-dev libffi-dev python3-dev

# -----------------------------------------------------------------------------------------------------------------
# Install PyEnv - PyEnv is a tool that allows you to install multiple versions of Python on the same machine
# -----------------------------------------------------------------------------------------------------------------
if [ -x "$(command -v pyenv)" ]; then
    printf "\nPyEnv is installed. Updating...\n"
    pyenv update
else
    printf "\nPyEnv is not installed. Installing...\n"
    # Install PyEnv
    curl https://pyenv.run | bash
    # Set up your shell environment for Pyenv
    printf "\nSetting up your shell environment for Pyenv...\n"
    # bashrc
    grep -qxF 'export PYENV_ROOT="$HOME/.pyenv"' ~/.bashrc || echo 'export PYENV_ROOT="$HOME/.pyenv"' >>~/.bashrc
    grep -qxF 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' ~/.bashrc || echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >>~/.bashrc
    grep -qxF 'eval "$(pyenv init -)"' ~/.bashrc || echo 'eval "$(pyenv init -)"' >>~/.bashrc
    # profile
    grep -qxF 'export PYENV_ROOT="$HOME/.pyenv"' ~/.profile || echo 'export PYENV_ROOT="$HOME/.pyenv"' >>~/.profile
    grep -qxF 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' ~/.profile || echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >>~/.profile
    grep -qxF 'eval "$(pyenv init -)"' ~/.profile || echo 'eval "$(pyenv init -)"' >>~/.profile
    # bash_profile
    grep -qxF 'export PYENV_ROOT="$HOME/.pyenv"' ~/.bash_profile || echo 'export PYENV_ROOT="$HOME/.pyenv"' >>~/.bash_profile
    grep -qxF 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' ~/.bash_profile || echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >>~/.bash_profile
    grep -qxF 'eval "$(pyenv init -)"' ~/.bash_profile || echo 'eval "$(pyenv init -)"' >>~/.bash_profile
fi

# -----------------------------------------------------------------------------------------------------------------
# Install Poetry - Poetry is a tool for dependency management and packaging in Python
# -----------------------------------------------------------------------------------------------------------------
# Unninstall Poetry if installed using the deprecated get-poetry.py script
printf "\nUninstalling Poetry if installed using the deprecated get-poetry.py script...\n"
rm -rf "${POETRY_HOME:-~/.poetry}"
export PATH=$(echo $PATH | sed -e 's#'"$HOME"'/.poetry/bin##g; s/::*/:/g; s/^://; s/:$//')
if [ -x "$(command -v poetry)" ]; then
    printf "\nPoetry is installed. Uninstalling to avoid locked version self update error...\n"
    curl -sSL https://install.python-poetry.org | python3 - --uninstall
fi
# Install Poetry
printf "\nPoetry is not installed. Installing...\n"
curl -sSL https://install.python-poetry.org | python3 -
# Set up your shell environment for Poetry
printf "\nSetting up your shell environment for Poetry...\n"
grep -qxF 'export PATH="$HOME/.local/bin:$PATH"' ~/.bashrc || echo 'export PATH="$HOME/.local/bin:$PATH"' >>~/.bashrc
grep -qxF 'export PATH="$HOME/.local/bin:$PATH"' ~/.profile || echo 'export PATH="$HOME/.local/bin:$PATH"' >>~/.profile
grep -qxF 'export PATH="$HOME/.local/bin:$PATH"' ~/.bash_profile || echo 'export PATH="$HOME/.local/bin:$PATH"' >>~/.bash_profile
# Enable tab completion for Bash
poetry completions bash >>~/.bash_completion
# Change config toc reate the virtualenv inside the project’s root directory
printf "\nChanging poetry config to create the virtualenv inside the project's root directory...\n"
poetry config virtualenvs.in-project true
poetry config virtualenvs.use-poetry-python true

# -----------------------------------------------------------------------------------------------------------------
# Install python with pyenv from .python-version file
# -----------------------------------------------------------------------------------------------------------------
printf "\nInstalling python version from .python-version file...\n"
pyenv install
pip install --upgrade pip setuptools wheel

# -----------------------------------------------------------------------------------------------------------------
# Create virtual environment for project
# -----------------------------------------------------------------------------------------------------------------
printf "\nCreating virtual environment for project...\n"
poetry sync
poetry env info
printf "\nInstalling pre-commit...\n"
poetry run pre-commit install
printf "\nPull DVC remote...\n"
poetry run dvc pull

# ---------------------------------------------------------------------------------------------------------------
# Final messages
# ---------------------------------------------------------------------------------------------------------------
printf "\nProject created successfully!\n"
printf "\nTo activate the virtual environment, run:\n"
printf "\npoetry env activate\n"
