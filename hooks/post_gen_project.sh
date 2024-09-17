#!/bin/sh
# -----------------------------------------------------------------------------------------------------------------
# If python_version is blank, then set it to the latest stable version of Python
# -----------------------------------------------------------------------------------------------------------------
if PYTHON_VERSION=$(pyenv install --list | egrep "^\s*{{cookiecutter.__python_version}}\." | tail -1 | xargs); then
    printf "\nInstalling $PYTHON_VERSION...\n"
else
    PYTHON_VERSION=$(pyenv install --list | egrep "^\s*3\.[0-9]{1,}\.[0-9]{1,}$" | tail -1 | xargs)
    printf "\nNo version of {{cookiecutter.__python_version}} found. Installing latest python version ($PYTHON_VERSION)...\n"
fi

# -----------------------------------------------------------------------------------------------------------------
# Install python_version
# -----------------------------------------------------------------------------------------------------------------
pyenv install $PYTHON_VERSION -s
pyenv global $PYTHON_VERSION

# -----------------------------------------------------------------------------------------------------------------
# Start a git repository if it not exists and copy .gitignore and .pre-commit-config.yaml
# -----------------------------------------------------------------------------------------------------------------
inside_git_repo="$(git rev-parse --is-inside-work-tree 2>/dev/null)"
if [ "$inside_git_repo" ]; then
    printf "\nGit repository already exists. Deleting .gitignore and .pre-commit-config.yaml...\n"
    rm -f .gitignore .pre-commit-config.yaml
else
    printf "\nInitializing new git repository...\n"
    git init -b main
fi

# -----------------------------------------------------------------------------------------------------------------
# Create virtual environment for project
# -----------------------------------------------------------------------------------------------------------------
printf "\nCreating virtual environment for project...\n"
poetry add fastapi pydantic-settings python-dotenv uvicorn hypercorn rich setuptools google-cloud google-cloud-logging
poetry add -G dev bandit black commitizen coverage docformatter dvc[gs] ipykernel ipywidgets isort jupyterlab mypy pdoc3 pre-commit pydocstyle pylint pytest pytest-xdist
poetry update
poetry install
poetry env info

# -----------------------------------------------------------------------------------------------------------------
# Install pre-commit
# -----------------------------------------------------------------------------------------------------------------
printf "\nInstalling pre-commit...\n"
poetry run pre-commit install
poetry run pre-commit install --hook-type commit-msg --hook-type pre-push --hook-type post-checkout --hook-type pre-commit
poetry run pre-commit autoupdate

# -----------------------------------------------------------------------------------------------------------------
# Initialize and configure dvc
# -----------------------------------------------------------------------------------------------------------------
printf "\nInitializing dvc...\n"
poetry run dvc init
poetry run dvc config core.autostage true
poetry run dvc remote add -d {{cookiecutter.dvc_remote_name}} {{cookiecutter.dvc_remote_url}}
echo README.md >> .dvcignore
poetry run dvc add data
poetry run dvc add models

# -----------------------------------------------------------------------------------------------------------------
# Run pre-commit
# -----------------------------------------------------------------------------------------------------------------
printf "\nRunning pre-commit...\n"
poetry run git add .
poetry run pre-commit run --all-files

# -----------------------------------------------------------------------------------------------------------------
# Git add and commit
# -----------------------------------------------------------------------------------------------------------------
printf "\nGit add and commit...\n"
poetry run git add .
poetry run git commit -m "feat: create template repository"

# -----------------------------------------------------------------------------------------------------------------
# Display success message
# -----------------------------------------------------------------------------------------------------------------
printf "\n{{cookiecutter.project_name}}[{{cookiecutter.__package_name}}] FastAPI project template created. Happy coding!\n\n"
