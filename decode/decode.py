# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
# http://docs.python-requests.org/en/latest/

# Note that I had to install this package using pip3, not pip.
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

for title in soup.find_all("h1"):
	print(title.find("a").text)