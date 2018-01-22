from __future__ import print_function

import requests

# Assign the url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Do the request thing (package, send and catch the response): r
r = requests.get(url)

# Decode JSON data: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)
