# {{cookiecutter.project_name}}
{{cookiecutter.description}}

## Tests
The tests can be run after installation with:
```sh
pytest
```
To verify coverage:
```sh
coverage run -m pytest
coverage report -m --fail-under 80
coverage html
```

## Google Cloud Setup
Please refer to the [Google Cloud Setup](docs/gcp_setup.md) document for instructions on how to setup a Google Cloud project.

## Deploy: Local
```sh
sudo docker build -t {{cookiecutter.__package_name}} -f pipelines/assembly/Dockerfile .
sudo docker run --env-file .env.example -p 8080:8080 {{cookiecutter.__package_name}}

# Stop all containers
sudo docker stop $(sudo docker ps -a -q)

# Override entrypoint and connect to container
sudo docker exec -it <container_id> /bin/bash
```

## Deploy: GCP
```sh
gcloud builds submit --config pipelines/assembly/cloudbuild.yaml .
```
