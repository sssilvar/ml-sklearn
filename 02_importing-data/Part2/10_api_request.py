from __future__ import print_function

import requests

# Assign the url
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'

# Package request, send it and get response
r = requests.get(url)

# Get JSON data into a dict: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ' : ', json_data[k])
