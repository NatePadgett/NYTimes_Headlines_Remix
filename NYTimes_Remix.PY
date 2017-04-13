import urllib
import json
import random

base_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?"
query_str = urllib.urlencode({ 
  "api-key": "de42c1616160470eb884f505b9ade18b",
  "q": "liberalism",
  "sort": "oldest"
})
request_url = base_url+query_str
#print request_url
response_str = urllib.urlopen(request_url).read()
response_dict = json.loads(response_str)
articles = response_dict['response']['docs']

#create one list for storing all of the lead paragraphs
leadp = []

for snippet in articles:
	#exclude one entry because it contains irregular
	#characters
	if '4fbfd23f45c1498b0d004e1b' not in snippet['_id']:
		#add the "lead_paragraph" section of each article
		#to the list leadp.
		leadp.append(snippet['lead_paragraph'])

#create a second list for storing the lines of each
#lead paragraph
lines = []

#split lines from the lead paragraphs
for line in leadp:
	line = line.strip()
	sentences = line.split("\n")

	#further split the lines at period
	for sentence in sentences:
		sentence = sentence.split(". ")
		
		#add split lines to lines list	
		for s in sentence:
			lines.append(s)

#print a random sample of lines and join at periods once
print ".\n\n ".join(random.sample(lines, 9))
	
