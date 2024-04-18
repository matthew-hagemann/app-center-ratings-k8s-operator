#! /bin/bash

set -euxo pipefail

TAG="sha-${1}"

charmcraft pack

juju refresh \
    app-ratings \
    --model=desktop \
    --path=./ubuntu-app-ratings_ubuntu-22.04-amd64.charm \
    --force-units \
    --resource "image=ghcr.io/tim-hm/app-center-ratings:$TAG"
