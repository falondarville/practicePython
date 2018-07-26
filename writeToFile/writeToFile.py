# Take the code from the How To Decode A Website exercise, and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

each_title = ""

for title in soup.find_all("h1"):
	each_title += title.find("a").text + " \n"
	print(each_title)

# Every time after a .write() statement, the file will be automatically saved. Use the method below or you will have to include a line to close the file after writing to it. This can potentially cause errors. 
# Note that you have to convert other types, like numbers and objects, to strings before adding them to a txt file. 
with open("write.txt", "w") as open_file:
	open_file.write(each_title)

