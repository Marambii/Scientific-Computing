# Python's built-in support for JSON
import json 
# Python turtle library for creating designs and images
import turtle  
# Python module for fetching URLs
import urllib.request  
# Python module for time-related functions
import time  
# Python module for opening URLs in a web browser
import webbrowser  
# Python module for retrieving latitude and longitude
import geocoder  

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

file = open("iss.txt", "w")
file.write(
    "There are currently " + str(result["number"]) +
    " astronauts on the ISS: \n\n"
)

people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")

# print long and lat
g = geocoder.ip('me')
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
screen.bgpic("images/map.gif")
screen.register_shape("images/iss.gif")
iss = turtle.Turtle()
iss.shape("images/iss.gif")
iss.setheading(45)
iss.penup()

while True: 
    # load the current status of the ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract the ISS location
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    # Output lon and lat to the terminal in the
    # float format
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # Update the ISS location on the map
    iss.goto(lon, lat)

    # Refresh each 5 seconds
    time.sleep(5)
