import ast
import socket 
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = '192.168.0.65'
port = 12000

server.connect((address, port))

action = None
body = None

while True:

    action = int(input('what do you want to do?\n(1)creat a task\n(2)delete a task\n(3)consult tasks\n=>'))

    if action == 1:
        title = input('what is a task title?\n=>')
        description = input('what is a task description?\n=>')
        
        action = 'push'
        body = {
            'title': title,
            'description': description
        }
    elif action == 2:
        title = input('what is a task title?\n=>')
        
        action = 'delete'
        body = {
            'title': title
        }
    elif action == 3:
        action = 'get'
        body = {}
    
    obj = {
        'action': action,
        'body': body
    }

    server.send(json.dumps(obj).encode('ascii'))

    response_data = server.recv(1024)

    try:
        obj_response = ast.literal_eval(response_data.decode('ascii'))
        for task in obj_response:
            print("\n")
            print('Task title: ',task['title'])
            print('Task description: ', task['description'])
            print("\n")
        if len(obj_response) == 0:
            print('\nNo task now\n')
    except:
        print('Received from the server :',str(response_data.decode('ascii')))

    ans = input('\nDo you want to continue(y/n) :')
    if ans == 'y':
        continue
    else:
        break

server.close()

