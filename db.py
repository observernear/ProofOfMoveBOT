import requests


res = requests.post(url='https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyAtPJQusY5DAvHLtFTn1BNd1NA-ikMbu9E')
print(res.json())