# regexAccounting.py

import re


def printRegexAccounting(text):
	accounts = re.findall(r'\b(\w+)\b\s+(\w+)\s+£(\d+.*\d*)', text)
	
	accountSums = {}

	for entry in accounts:
		if entry[0] in accountSums:
			if entry[1] == 'received':
				accountSums[entry[0]] += float(entry[2])
			elif entry[1] == 'spent':
				accountSums[entry[0]] -= float(entry[2])
		else:
			if entry[1] == 'received':
				accountSums[entry[0]] = float(entry[2])
			elif entry[1] == 'spent':
				accountSums[entry[0]] = 0-float(entry[2])

	print(''' ----summary----''')
	for key in accountSums:
		print("{} has £{}".format(key,accountSums[key]))




def main():
	text='''Tutu received £5
	Cici received £10
	Cici spent £1.90
	Tutu spent £1.50
	Tutu spent £1
	Didi received £3.00
	Didi received £2.90
	Didi spent £0.90'''

	printRegexAccounting(text)

if __name__ == '__main__':
	main()