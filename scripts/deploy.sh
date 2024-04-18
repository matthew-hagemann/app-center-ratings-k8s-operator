#! /bin/bash

set -euxo pipefail

TAG="sha-${1}"

charmcraft pack

juju deploy \
    ./ubuntu-app-center-ratings_ubuntu-22.04-amd64.charm \
    app-ratings \
    --model=desktop \
    --resource "image=ghcr.io/tim-hm/app-center-ratings:$TAG"
