from controllers.tasks_controller import deleteTask
from controllers.tasks_controller import createTask
from database import tasks
import socket
import ast

from _thread import *
import threading

print_lock = threading.Lock()


def client_connection(request_data):
    while True:
        data = request_data.recv(1024)
        if not data:
            print('user desconnect')
            print_lock.release()
            break

        try:
            client_request = ast.literal_eval(data.decode())

            print('client request => ',client_request)
            if client_request['action'] == 'get':
                request_data.send(str(tasks).encode('ascii'))

            elif client_request['action'] == 'push':
                title = client_request['body']['title']
                description = client_request['body']['description']
                request_data.send(createTask(title, description).encode('ascii'))

            elif client_request['action'] == 'delete':
                title = client_request['body']['title']
                request_data.send(deleteTask(title).encode('ascii'))

        except:
            print('no data now')

    request_data.close()

port = 12000
host = ''

esperando = input('Press enter to start server')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print("socket binded to port", port)

while True:
    request_data, address = server.accept()
  
    print_lock.acquire()
    print('Connected to :', address[0], ':', address[1])

    start_new_thread(client_connection, (request_data,))