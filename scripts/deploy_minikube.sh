#! /usr/bin/env sh

# Exit in case of error
set -e

CONF_MAP=grover-challenge

# we're using minkubes docker-service to be able to run with
# local images
eval $(minikube docker-env)

INSTALL_DEV=false docker-compose -f docker-compose.yml build

# if there exists already a configmap, delete
if kubectl get configmap $CONF_MAP >/dev/null 2>&1
then 
  kubectl delete configmap $CONF_MAP
fi

kubectl create configmap $CONF_MAP --from-env-file .env
kubectl apply -f minikube

echo "\n...Done!"
echo "Visit service-docs at: `minikube service grover-challenge --url`/docs (might take a moment)"
