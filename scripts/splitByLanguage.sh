#!/bin/bash
awk -F '\t' '{ if($2 == "es" || $2 == "en") {filename=$2".tsv"; print $1 >> filename} }' $1