# cookiecutter-fastpi

A [cookiecutter](https://cookiecutter.readthedocs.io/) template for FastAPI.  This template allows for the easy creation of a full project directory that is both language- and cloud-agnostic.

## Usage

1.  Make sure you have git and [cookiecutter](https://cookiecutter.readthedocs.io/) installed by running the following commands in your terminal:
    * `sudo apt update && sudo apt install git -y`
    * `python3 -m pip install --upgrade pip`
    * `python3 -m pip install --user cookiecutter`
2.  Generate your project using the project template from this repository. You will be prompted for: **project name**, **customer/client name**, **description**, **authors** and **license**.
    * `cookiecutter https://github.com/lucasmtz/cookiecutter-fastapi`
        * **project_name** [Project Name]: `propensity-buy-ecommerce`
        * **customer_name** [Customer or Client Name]: `Some Big Company`
        * **description** [Project descriprion]: `A data science project for a big company`
        * **authors:** [author1_name <author1_email>, author2_name <author2_email>]: `author1 <author1@example.com>, author2 <author2@example.com>`
        * **license** [Choice Variable]: `1`
        * **python_version** [3.11]: 3.8+ (latest). If input is not valid the default is the latest version of python 3.
        * **dvc_remote_name** [DVC remote name]: `gcs`
        * **dvc_remote_url** [DVC remote url]: `gs://my-bucket` *GCS is preffered as this template is designed to work with GCP. Note: You have to create the bucket before running the project.*
3.  The project directory will be created in the current directory.  You can navigate to the project directory using the `cd` command and open VS Code using the `code` command.
    * `cd propensity_buy_ecommerce`
    * `code .`
