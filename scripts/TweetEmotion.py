from __future__ import print_function
from multiprocessing import Pool 
import sys

expanded_anew = {}
i = 0
with open('../data/expandedANEW.csv') as inpt:
	for line in inpt:
		if i == 0:
			i = 1
			continue

		line = line.strip().split(",")
		expanded_anew[line[0]] = line[1:]

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

def process_line(line):
	try:
		tid, uid, date, tweet = line.strip().split("\t")
		values = [expanded_anew[token] for token in tweet.split(" ") if token in expanded_anew]
		return "{}\t{}\t{}\t{}".format(tid, uid, date, values)
	except Exception, e:
		warning("Error in line: {}, {}".format(line, e))

pool = Pool(4)
with open('../demo/ObamaTweets_bydate.tsv.neg.preprocessed') as inpt:
	results = pool.map(process_line, inpt, 4)

for r in results:
	print(r)



