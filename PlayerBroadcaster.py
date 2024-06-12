import socket
import random
import json
from socket import *
from time import sleep

serverName = '255.255.255.255'
serverPort = 10100
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

playersData = {
    "id": 1,
    "firstName": "New",
    "lastName": "Player",
    "number": random.randint(1, 99),  # Random number from 1 to 99
    "position": "Forward"
}

while True:
    # Update player's number with a random value
    playersData["number"] = random.randint(1, 99)
    
    # Convert to JSON
    jsonData = json.dumps(playersData)
    print(jsonData)
    
    # Send the JSON data via UDP broadcast
    clientSocket.sendto(jsonData.encode(), (serverName, serverPort))
    
    # Wait for a random period of time
    sleep(random.randint(1, 5))