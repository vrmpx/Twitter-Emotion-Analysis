from datetime import datetime

curr_key = None
curr_dict = None 

with open('mapper.results') as inpt:
	for line in inpt:
		key, val = line.strip().split("\t")
		lon, lat, val, aro = eval(val) 
		
		if curr_key == key:	

			


		else:
			if curr_key:
				print "{}\t{}".format(curr_key, curr_dict)

			


if curr_key == key:
	print "{}\t{}".format(curr_key, curr_dict)