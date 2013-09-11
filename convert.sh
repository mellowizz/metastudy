#!/usr/bin/bash


for f in $@; do
    eval "pdftotext $f ${f%.pdf}.txt"
done

