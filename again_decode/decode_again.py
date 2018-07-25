# print all of the text on the page
import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

# note that the text is divided in many divs with data-reactid attributes. 
results = soup.get_text("span", {"data-reactid", "169"})

print(results)
