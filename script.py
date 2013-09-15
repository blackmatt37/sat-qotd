from bs4 import BeautifulSoup
import urllib

url = "http://sat.collegeboard.org/practice/sat-question-of-the-day"
# print urllib.urlopen(url).read()
soup = BeautifulSoup(urllib.urlopen(url).read())
qcontainer = soup.find(id="qotdQuestionContainer")
question = qcontainer.find('div').find_all('p', recursive=False)
for q in question:
	print q.get_text().encode('ascii', 'ignore')

for x in qcontainer.fieldset.find_all('label'):
	print x.string
