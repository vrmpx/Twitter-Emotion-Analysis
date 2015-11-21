from multiprocessing import Pool

def mapper(line):
	date, us_valence, us_arousal, mx_valence, mx_arousal = line.strip().split(",")
	
	try:
		tmp = date.split("/")
		month = tmp[0]
		day = tmp[1]
		year = tmp[2].split(" ")[0]

		return ((day, month, year), (us_valence, us_arousal, mx_valence, mx_arousal))
	except:
		return None

def reducer(monthpairs):
	

def main():
	p = Pool(4)
	with open('results.csv') as inpt:
		monthpairs = p.map(mapper, inpt)



if __name__ == '__main__':
	main()