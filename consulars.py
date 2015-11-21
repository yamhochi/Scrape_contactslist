import urllib.request
from bs4 import BeautifulSoup
f = open("/Users/hoecheeyam/Desktop/dfat/all_consulars.txt",'w')

#create a python list from the list of urls copied
with open("/Users/hoecheeyam/Desktop/dfat/urls_clean.txt","r") as urls:
	url_list=urls.readlines()
for link in url_list:
	url="http://protocol.dfat.gov.au/Consulate/"+link
	page=urllib.request.urlopen(url)
	soup=BeautifulSoup(page)

	#title
	title=soup.find("div",{"id":"mainTitles"}).text.strip()
	
	#get address
	table=soup.find("table")
	td=table("td")
	address=' '.join(td[0].text.split())

	f.write(title+'\n')
	f.write(title+':'+'Address: '+address+'\n')

	# create a sub-html section for under office details (table and business hours)
	office_details_html=soup.find("div",{"class":"officeDetails"})
	# create a list to store divs under the sub html
	list_office_divs=office_details_html.findAll("div")
	#for each of those divs print the enclsed text
	for i in list_office_divs:
	   # each_div=i.get_text().strip()
	   each_div =' '.join(i.get_text().split())
	   f.write(title+':'+each_div+'\n')	    

	#create sub-htmls section for officers. returns a list object
	officers_htmls=soup.findAll("div",{"class":"officer"})
	for html in officers_htmls:
	   StringsOfEachHTML=html.get_text()
	   consular_title=html.find("div").get_text()
	   output_names=' '.join(StringsOfEachHTML.split())
	   output_titles = ' '.join(consular_title.split())
	   f.write(title+':'+output_titles+':'+output_names+'\n')

f.close()





