# Google Cloud Setup
This document describes the steps required to setup a Google Cloud project for development and production of the **Nutshell application**.

## Install the Google Cloud SDK
We [install the Google Cloud SDK](https://cloud.google.com/sdk/docs/downloads-snap
) locally in order to have access to commands such as `bq` (bigquery dataset and table management) and `gsutil` (google cloud storage) and also to be able to use google cloud services to locally run processes during development. Bear in mind though that Google Cloud provides a shell that can be invoked from the Console, which is already equipped with commands and authentication.

## Google Cloud Project Access
**Execute gcloud init to establish a link to a Google Cloud project.**
```bash
gcloud init
```
This will trigger authentication against your google account and then present you with the projects you have access to.

Create as many [configurations](https://cloud.google.com/sdk/gcloud/reference/config/configurations/create) as projects you will regularly access and the recommendation is to name a configuration the same as the project it refers to.

**To activate a configuration use:**
```bash
gcloud config configurations activate <CONFIG NAME>
```

**To check which configuration is active, use:**
```bash
 gcloud config configurations  list
```

Configurations are relevant in the following example use cases:

* Tools such as `bq` and `gsutil` will display the resources of the project the active configuration is attached to.
* Deployment tools will by default point to the configuration’s project.

## Application Authentication
Production applications use a service account, the default one implicit in services like compute engine or cloud functions, or an explicit one.

When running things locally we consider it is acceptable to access services as the personal user (this way we have somebody to blame for the damage!).

To be able to do so you must authenticate against google cloud with:
```bash
gcloud auth application-default login
```

## Enable Required APIs
Enable the required APIs for your project by running the following commands:
```bash
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

# Grant Cloud Run Administrator and Administrador de Artifact Registry role to the Cloud Build service account
https://console.cloud.google.com/cloud-build/settings
