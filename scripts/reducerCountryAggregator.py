from datetime import datetime
from multiprocessing import Pool

curr_key = None
curr_dict = None 

with open('mapper.results') as inpt:
	for line in inpt:
		key, val = line.strip().split("\t")
		country, valence, arousal = eval(val) 
		
		if curr_key == key:	

			curr_dict[country][0] += float(valence)
			curr_dict[country][1] += float(arousal)
			curr_dict[country][2] += 1


		else:
			if curr_key:
				print "{}\t{}".format(curr_key, curr_dict)

			curr_key = key
			curr_dict = {"MX":[0.0, 0.0, 0], "US":[0.0, 0.0, 0], "BR":[0.0, 0.0, 0], "PH":[0.0, 0.0, 0]} #This is horrible but I got no better idea 
			curr_dict[country] = [float(valence), float(arousal), 1]


if curr_key == key:
	print "{}\t{}".format(curr_key, curr_dict)
