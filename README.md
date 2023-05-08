# Simple Socket Calculator
A simple calculator using sockets to calculate basic mathematical expressions.

## Allowed operations:
- Sum: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Exponentiation: `**`

## Requirements
Python 3.x

## Install python
### Ubuntu
`sudo apt-get install python3`

### Arch
`sudo pacman -S python3`

## Usage
For testing locally: 
1. run server.py `python server.py` 
2. run client.py `python client.py`
3. set Host=127.0.0.1 and Port=12345

For testing with different machines:
1. Gather at least 2 machines (server and client)
2. on the server machine run `ip addr` (linux) or `ipconfig` (windows) and get your local ip
3. run server.py on a machine (server) `python server.py`
4. run client.py on another machine `python client.py`
5. set Host=`the local ip of the server` and Port=12345

## Valid inputs examples
- 5 + 100
- (39 + 21) - 13 * 2
- 4 ** 2 - 14 / 2 <br>
(Spaces are optional)
