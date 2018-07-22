# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
# http://docs.python-requests.org/en/latest/

# Note that I had to install this package using pip3, not pip.
import requests

r = requests.get('https://www.nytimes.com/')

print(r)