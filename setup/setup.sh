#!/bin/bash

OLDWD=$(pwd) 
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P)"

cd $SCRIPTPATH
cd ..

{
    python3 -m venv messenger-cli/messenger_environment
    source messenger-cli/messenger_environment/bin/activate
    pip3 install fbchat switchcase
} &> /dev/null

cd $OLDWD