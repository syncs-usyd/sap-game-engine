#!/bin/bash

export GAME_ENGINE_CORE_DIRECTORY=/var/competition

directory=$(realpath $(dirname $(dirname "$0")))
cd $directory/engine
./env/bin/python3 -m engine 2>$directory/output/engine.err
