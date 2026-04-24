from rcon.source import Client

RCON_HOST = '192.168.1.41'
RCON_PORT = 27015
RCON_PASSWORD = 'asdf1234password'

def rcon_command(command):
    try:
        with Client(RCON_HOST, RCON_PORT, passwd=RCON_PASSWORD) as client:
            return {'ok': True, 'result': client.run(command)}
    except Exception as e:
        return {'ok': False, 'error': str(e)}
    
# get command from user and run it
command = input("Enter RCON command: ")
result = rcon_command(command)
# result looks like json, so lets decode it and print the result
import json
try:
    data = json.loads(result['result'])
    print("Command output:")
    print(json.dumps(data, indent=2))
except Exception as e:
    print("Error decoding command output:", e)
    print("Raw output:")
    print(result['result'])