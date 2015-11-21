#!/bin/bash

python ../../scripts/mapperCountryAggregator.py > mapper.results

gsort mapper.results > tmp 
mv tmp mapper.results



python ../../scripts/reducerCountryAggregator.py > reducer.results