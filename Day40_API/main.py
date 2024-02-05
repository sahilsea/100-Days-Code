import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')

data = response.json()

latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

print((latitude, longitude))