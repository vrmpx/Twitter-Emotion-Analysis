#!/bin/bash 
gtr -cs 'a-zA-Z' ' ' < $1 | gtr ' ' '\012' | sort | uniq -c