#!/bin/bash

for f in $@; do
    if [ ! -f ${f%.pdf}.txt ]
    then
        echo "no pdf of" $f
        #eval "rm $f"
    fi
done
