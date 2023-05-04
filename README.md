# pythonSocketCalculator
Simple Socket Calculator

## Requirements
Python 3.x

## Usage
For testing locally: 
1. run server.py 
2. run client.py
3. set Host=127.0.0.1 and Port=12345

For testing with different machines:
1. Gather at least 2 machines (server and client)
2. on the server machine run "ip addr" (linux) or "ipconfig" (windows) and get your local ip
3. run server.py on a machine (server)
4. run client.py on another machine
5. set Host=<the local ip of the server> and Port=12345
