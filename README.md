## GKE Private cluster
To create private cluster in GKE, run
```bash
export GOOGLE_APPLICATION_CREDENTIALS=<Path to your Google credentials json file>
./auto/create_private_gke_cluster.sh
```
By default, it will take the default values in the script, you can also add the values to the environment variables below and run:

```bash
export PROJECT=
export REGION=
export ZONE=
export SUBNETWORK=
export SUBNETWORK_SECONDARY_RANGE_NAME=
export SERVICE_ACCOUNT_EMAIL=
export GOOGLE_APPLICATION_CREDENTIALS=<Path to your Google credentials json file>
./auto/create_private_gke_cluster.sh
```

# Build application and push Image to GCR
To Build application and push the image to GCR, run :
```bash
./auto/build
```

## Helm Application Deployment
To deploy application using Helm in Dev:
```bash
helm install ./infra -f infra/dev.yaml
```

Note: pass the environment file such as dev.yaml, staging.yaml, prod.yaml to deploy the application in Dev, Staging and production environments.

## Run locally
To run the application locally,run :
```bash
./auto/run
```


