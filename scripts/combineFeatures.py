from __future__ import print_function
from multiprocessing import Pool 
import sys
import numpy as np 
import math

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)


def mapper(line):
	try:
		tweetID, from_user_id, created_at, Arousal_Valence_Mtx = line.strip().split('\t')
		Arousal_Valence_Mtx = eval(Arousal_Valence_Mtx)

		if len(Arousal_Valence_Mtx) > 1:
			arousal, arousal_std, freq, valence, valence_std = zip(*map(lambda x: (float(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4])), Arousal_Valence_Mtx))

			#TODO: combine values
			Mv = sum([f * m for f, (m, s) in zip(freq, zip(valence, valence_std))]) / sum(freq)
			Ma = sum([f * m for f, (m, s) in zip(freq, zip(arousal, arousal_std))]) / sum(freq)

			return "{}\t{}\t{}\t{}\t{}".format(tweetID, from_user_id, created_at, Mv, Ma)

		return "{}\t{}\t{}\t{}\t{}".format(tweetID, from_user_id, created_at, "0.0", "0.0")

	except Exception, e:
		warning("Error in line: {}, {}".format(line, e))


pool = Pool(4)
header = False
with open('../demo/ObamaTweets_valence_arousal.tsv') as inpt:

	if header:
		next(inpt)

	results = pool.map(mapper, inpt)

	for r in results:
		print(r)
