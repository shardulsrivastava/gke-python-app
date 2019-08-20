#!/usr/bin/env bash

set -euxo pipefail

cd $(dirname $0)/../terraform

export DEFAULT_PROJECT=data-services-asia-dev
export DEFAULT_REGION=asia-northeast1
export DEFAULT_ZONE=asia-northeast1-a
export DEFAULT_NETWORK=reaasia-dataservices-dev-vpc
export DEFAULT_SUBNETWORK=reaasia-dataservices-private-tokyo-dev-subnet
export DEFAULT_SUBNETWORK_SECONDARY_RANGE_NAME=gke-private-cluster-pods-561fbd26
export DEFAULT_SERVICE_ACCOUNT_EMAIL=341208819623-compute@developer.gserviceaccount.com

cat > ./terraform.tfvars <<EOF
project       = "${PROJECT:-$DEFAULT_PROJECT}"
region        = "${REGION:-$DEFAULT_REGION}"
location      = "${ZONE:-$DEFAULT_ZONE}"
network       = "${NETWORK:-$DEFAULT_NETWORK}"
subnetwork    = "${SUBNETWORK:-$DEFAULT_SUBNETWORK}"
subnetwork_secondary_range_name = "${SUBNETWORK_SECONDARY_RANGE_NAME:-$DEFAULT_SUBNETWORK_SECONDARY_RANGE_NAME}"
service_account_email = "${SERVICE_ACCOUNT_EMAIL:-$DEFAULT_SERVICE_ACCOUNT_EMAIL}"
EOF

terraform init -input=false 
terraform plan -out=tfplan -input=false
terraform apply -input=false tfplan