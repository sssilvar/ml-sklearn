from __future__ import print_function

import requests
from bs4 import BeautifulSoup


# Specify the url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc, 'html.parser')

# Prettify the BeautofulSoup object: pretty_soup
pretty_soup = soup.prettify()

# Print the result
print('\n\n UGLY WAY!!! \n\n', html_doc)
print('\n\n PRETTYFIED WAY!!! \n\n', pretty_soup)

# # Save them as HTML files
# with open('html_doc.html', 'w') as file:
#     file.write(html_doc)
#
# with open('pretty_soup.html', 'w') as file:
#     file.write(pretty_soup)
