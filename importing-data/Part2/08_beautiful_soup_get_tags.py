from __future__ import print_function

import requests
from bs4 import BeautifulSoup

# Specify the url
url = 'https://www.python.org/~guido/'

# Package the request, send it and get the response: r
r = requests.get(url)

# Get the HTML code: html_doc
html_doc = r.text

# Create a BeautifulSoup: soup
soup = BeautifulSoup(html_doc, 'html.parser')

# Print the title of the page
print(soup.title)

# Find all <a> tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
print('\n\n[INFO] These are the urls found in the request: \n')
for link in a_tags:
    print(link.get('href'))
