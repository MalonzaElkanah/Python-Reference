import requests, bs4

path = '/home/malone/websites/betscrapper/defa/mobile.betlion.ke/Home/Highlights.html'
file = open(path)
soup = bs4.BeautifulSoup(file)
elnts = soup.select('.BLM-matchBox')
for elnt in elnts:
	raw_data = elnt.getText()
	lists = raw_data.split('\n')
	new_list = []
	for l in lists:
		if not l == "":
			new_list = new_list + [l]
	print(new_list)


#['Arsenal', 'Norwich', '+187', '#73831', '1.44', '4.75', '8.00']
