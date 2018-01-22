from __future__ import print_function

from six.moves.urllib.request import Request, urlopen


# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print type of response
print(type(response))

# Extract the response: html
html = response.read()

# Print the response HTML and close the response
print(html)
response.close()