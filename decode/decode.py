# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
# http://docs.python-requests.org/en/latest/

# Note that I had to install this package using pip3, not pip.
import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

r = requests.get('https://www.nytimes.com/')

soup.h1["story-heading"].a

print(r)