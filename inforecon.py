#This python script can be used for information gathering on a host name
"""The requests module here is used for banner grabbing.
A technique of grabbing information of a system available on a certain network, can include all open ports.
"""
import sys
import requests
import socket
import json

#incase no argument is provided in the command line, this is to help the user know to use the code
#A basic help message
#sys.argv[0] is the name of the script
#GRABBING BANNERS

if len(sys.argv) < 2:
    print("Usage: "+sys.argv[0] + "<url>")
    sys.exit(1)

#sys.argv[1] is the domain we will provide as a command line argument
req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

#HOSTNAME
#To get the hostname we use the socket module
#We use the gethostbyname() function which is in the socket module
gethost_ = socket.gethostbyname(sys.argv[1])
print("\n The IP Address of "+sys.argv[1]+" is: "+gethost_ + "\n")

#IP LOOKUP
#ipinfo.io api helps us in our IP lookup
#For IP lookup we want to identify the latitude and longitude
req_two = requests.get("https://ipinfo.io/"+gethost_+"\n")
resp_ = json.loads(req_two.text)

print("Location: "+resp_["loc"])
print("Region: "+resp_["region"])
print("City: "+resp_["city"])
print("Country: "+resp_["country"])
