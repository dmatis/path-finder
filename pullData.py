import urllib.request

url = "http://data.vancouver.ca/download/kml/bikeways.kmz"
print("why")


def download_data():
    print("hello")
    urllib.request.urlretrieve(url, "bikeways.kmz")

download_data()
