import http.client

conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "16975a2b67msh091c47ae8a93211p16bd10jsndfe90fb8f967"
    }

conn.request("GET", "/weather?callback=test&id=2172797&units=%22metric%22%20or%20%22imperial%22&mode=xml%2C%20html&q=London%2Cuk", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))