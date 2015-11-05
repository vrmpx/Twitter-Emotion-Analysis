#!/bin/bash

gtr '[:upper:]' '[:lower:]' < $1 > $1.lower
gsed -i.bak -e 's|http[^ ]*\/[^ ]*\b|__URL__|g' $1.lower
gsed -i.bak -e 's|@[^ ]*\b|__MENTION__|g' $1.lower
gsed -i.bak -e 's|\b[0-9][0-9][0-9][0-9]\b|__4NUM__|g' $1.lower
gsed -i.bak -e 's|\b[0-9]+\b|__NUM__|g' $1.lower
gtr -dc "[:alnum:][:space:]'@#_\n" < $1.lower > $1.lower.preprocessed
