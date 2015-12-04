from multiprocessing import Pool
from datetime import date, datetime, timedelta
from nltk.corpus import stopwords

# print "================ uid2country ================"

uid2country = {}
with open("./countryData/countryInference_user.tsv") as inpt:
	for line in inpt:		
		uid, _, _, country = line.strip().split("\t")
		uid2country[uid] = country

stopWords = stopwords.words('english')

def mapper(line):
	try:
		_, uid, D, tweet = line.strip().split("\t")

		########
		# Do something with the date
		########
		D = datetime.strptime(D, "%a %b %d %H:%M:%S +0000 %Y")
		#Time zone diff
		D = D - timedelta(hours = 8)
		#Remove seconds and useless info
		# date = datetime.strftime(date, "%m/%d/%y %H:%M")

		country = uid2country[uid]

		if country != "US":
			return None

		# if date(2014, 4, 8) <= D.date() <= date(2014, 4, 9):
		if date(2013, 12, 24) == D.date() <= date(2013, 12, 25):
			return "{}\t{}\t{}".format(D, country, tweet)

		return None 
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

with open("./tweets_users_date_EN.tsv.preprocessed") as inpt:
	results = p.map(mapper, inpt)
	for r in results:
		if r:
			print r