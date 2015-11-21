from glob import iglob as glob
from multiprocessing import Pool
from datetime import datetime, timedelta

# print "================ uid2country ================"

uid2country = {}
with open("../data/countryData/countryInference_user.tsv") as inpt:
	for line in inpt:		
		uid, _, _, country = line.strip().split("\t")
		uid2country[uid] = country

# print "Len: ", len(uid2country)

def mapper(line):
	try:
		_, uid, date, val, aro = line.strip().split("\t")

		########
		# Do something with the date
		########
		date = datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y")
		#Time zone diff
		date = date - timedelta(hours = 8)
		#Remove seconds and useless info
		date = datetime.strftime(date, "%m/%d/%y %H:%M")

		country = uid2country[uid]

		if country != "MX" or country != "US":
			return None

		return "{}\t('{}',{},{})".format(date, country, val, aro)
	except:
		return None


# Test using head -n 50 Tweets_Valence_Arousal_EN.tsv | python ../scripts/mapperCountryAggregator.py
# import sys
# for line in sys.stdin:
# 	r = mapper(line)
# 	if r:
# 		print r 

#Real deal 
p = Pool(4)

for f in glob("../data/Tweets_Valence_Arousal_E*.tsv"):
	# print "Reading ", f

	with open(f) as inpt:
		results = p.map(mapper, inpt)
		for r in results:
			if r:
				print r
