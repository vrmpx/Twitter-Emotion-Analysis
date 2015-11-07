#!/bin/bash

#Process negations
# cat $1 | ./negation > $1.neg

#Clean NEG_#
gsed -i -e 's|NEG_#|#|g' $1

#lowercase
gtr '[:upper:]' '[:lower:]' < $1 > $1.lower

#Tokenize URL
gsed -i.bak -e 's|http[^ ]*\/[^ ]*\b|__URL__|g' $1.lower
# gsed -i.bak -e 's|neg_http[^ ]*\/[^ ]*\b|__URL__|g' $1.lower

#Tokenize mentions
gsed -i.bak -e 's|neg_@[^ ]*\b|__MENTION__|g' $1.lower
gsed -i.bak -e 's|@[^ ]*\b|__MENTION__|g' $1.lower

#Tokenize numbers 
gsed -i.bak -e 's|\b(neg_)?[0-9][0-9][0-9][0-9]\b|__4NUM__|g' $1.lower
gsed -i.bak -e 's|\b[0-9][0-9][0-9][0-9]\b|__4NUM__|g' $1.lower
gsed -i.bak -e 's|\b(neg_)?[0-9]+\b|__NUM__|g' $1.lower
gsed -i.bak -e 's|\b[0-9]+\b|__NUM__|g' $1.lower

#Remove odd punct
gtr -dc "[:alnum:][:space:]'@#_\n" < $1.lower > $1.lower.preprocessed