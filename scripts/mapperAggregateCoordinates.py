from glob import iglob as glob
from multiprocessing import Pool
from datetime import date, datetime, timedelta


uid2country = {}
with open("./countryData/countryInference_user.tsv") as inpt:
	for line in inpt:		
		uid, lon, lat, country = line.strip().split("\t")
		if country == "MX" or country == "US":
			uid2country[uid] = (country, (lon, lat))

def mapper(line):
	try:
		_, uid, D, val, aro = line.strip().split("\t")

		if val == 0.0 or val == "0.0":
			val = 5.0

		if aro == 0.0 or aro == "0.0":
			aro = 5.0

		########
		# Do something with the date
		########
		D = datetime.strptime(D, "%a %b %d %H:%M:%S +0000 %Y")
		#Time zone diff
		D = D - timedelta(hours = 8)
		#Remove seconds and useless info

		country, (lon, lat) = uid2country[uid]
		
		if date(2013, 12, 25) <= D.date() <= date(2013, 12, 26):
			D = datetime.strftime(D, "%m/%d/%y %H:%M")
			return "{}\t{}\t{}\t{}\t{}".format(uid, D, country, val, aro)

	except:
		return None

# Test using head -n 50 Tweets_Valence_Arousal_EN.tsv | python ../scripts/mapperAggregateCoordinates.py
# import sys
# for line in sys.stdin:
# 	r = mapper(line)
# 	if r:
# 		print r 

#Real deal 
p = Pool(4)

for f in glob("./Tweets_Valence_Arousal_E*.tsv"):
	# print "Reading ", f

	with open(f) as inpt:
		results = p.map(mapper, inpt)
		for r in results:
			if r:
				print r