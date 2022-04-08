#!/bin/bash

cd packages/core; npm i && npm run build; cd ../..

cd packages/cli

npm i && npm run build

npx pkg -t node16-linux-x64 -o dist/placebot-linux-amd64 dist/index.js
npx pkg -t node16-windows-x64 -o dist/placebot-windows-amd64 dist/index.js

cd ../..