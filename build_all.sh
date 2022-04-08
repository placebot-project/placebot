#!/bin/bash

cd packages/core; npm i && npm run build; cd ../..
cd packages/cli; npm i && npm run build; cd ../..