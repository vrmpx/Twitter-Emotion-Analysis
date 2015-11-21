print "date,us_valence,us_arousal,mx_valence,mx_arousal"
with open('reducer.results') as inpt:
	for line in inpt:
		key, dic = line.strip().split("\t")
		dic = eval(dic)

		if dic["US"][2] == 0:
			val_us = 0.0
			aro_us = 0.0
		else:
			val_us = float(dic["US"][0]) / dic["US"][2]
			aro_us = float(dic["US"][1]) / dic["US"][2]

		if dic["MX"][2] == 0:
			val_mx = 0.0
			aro_mx = 0.0
		else:
			val_mx = float(dic["MX"][0]) / dic["MX"][2]
			aro_mx = float(dic["MX"][1]) / dic["MX"][2]



		print "{},{},{},{},{}".format(key, val_us, aro_us, val_mx, aro_mx)

