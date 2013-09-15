from bs4 import BeautifulSoup
import urllib, urllib2

get_url  = "http://sat.collegeboard.org/practice/sat-question-of-the-day"
post_url = "http://sat.collegeboard.org/practice/answered-question-of-the-day"
# print urllib.urlopen(url).read()
soup = BeautifulSoup(urllib.urlopen(get_url).read())
qcontainer = soup.find(id="qotdQuestionContainer")
question = qcontainer.find('div').find_all('p', recursive=False)
for q in question:
	print q.get_text().encode('ascii', 'ignore')

for x in qcontainer.fieldset.find_all('label'):
	print x.string

data="pageId=practiceQOTD&hintUsed=false&qotdSubmit=Submit"
# select = "E"
select = raw_input("Selection: ")
print ""
data += "&userResponse=" + select
req = urllib2.Request(post_url, data)
response = BeautifulSoup(urllib2.urlopen(req).read())
footer = response.find(id="qotdQuestionFooter")
if footer.find('h1') != None:
	print footer.find('h1').get_text()
if footer.find(id="qotdExplanation") != None:
	print footer.find(id="qotdExplanation").get_text().encode('ascii', 'ignore')
else:
	print footer.find(id="qotdQuestionResult").get_text().encode('ascii', 'ignore')

