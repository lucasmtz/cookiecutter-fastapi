# `cookiecutter-fastpi`: FastAPI Project Generator

Introducing `cookiecutter-fastpi`: a template for [FastAPI](https://fastapi.tiangolo.com/) powered by [cookiecutter](https://cookiecutter.readthedocs.io/). This template simplifies the process of initializing a versatile project directory. It's designed to be language-neutral and cloud-platform agnostic.

## How to Use

### Prerequisites
1. **Install `git` and `cookiecutter`:** Before generating your FastAPI project, ensure you have both `git` and `cookiecutter` installed:
    * Update your packages: `sudo apt update && sudo apt install git -y`
    * Upgrade pip (Python package installer): `python3 -m pip install --upgrade pip`
    * Install `cookiecutter`: `python3 -m pip install --user cookiecutter`

### Generating a New FastAPI Project
2. **Create your FastAPI project:** Use the template from this repository. During this step, you'll be prompted for details like project name, customer/client details, description, author information, and more:
    ```bash
    cookiecutter https://github.com/lucasmtz/cookiecutter-fastapi
    ```

    * Example prompts:
        * **Project Name**: `propensity-buy-ecommerce`
        * **Customer or Client Name**: `Some Big Company`
        * **Project Description**: `A data science project for a big company`
        * **Authors**: `John Doe,Jane Doe`
        * **Author Emails**: `johndoe@example.com,janedoe@example.com`
        * **License Choice**: `1`
        * **Python Version**: `x`, `x.x` or `x.x.x` (If provided input isn't valid, it defaults to the most recent Python 3.x version.)
        * **DVC Remote Name**: `YourChosenName`
        * **DVC Remote URL**: This can be a local path or [remote storage](https://dvc.org/doc/user-guide/data-management/remote-storage#supported-storage-types). Examples: `gs://my-bucket` or `/path/to/local/storage`. If you choose a remote storage, ensure the remote location has been set up before executing. Using remote storage is recommended for collaborative projects.
> **Note**: This template initializes various configurations, such as updating `apt`, setting up `pyenv`, `poetry`, installing dependencies, setting up pre-commit hooks, initializing `dvc`, and creating the initial commit. If any of these configurations aren't required, or if you wish to make modifications, you should fork the repository and then adjust or remove items from the `hooks` directory accordingly.

### Post-Generation Steps
3. **Access your new project directory**: Once the project is generated, navigate to its directory and optionally open it in Visual Studio Code:
    ```bash
    cd propensity_buy_ecommerce
    code .
    ```

By following these steps, you're on your way to developing a robust FastAPI project. Happy coding!
