import json
import socket
from threading import Thread

sever_thread = None
TOPOLOGY_TABLE = None


def showPrompt():
    print("init -t <file-name> -i <interval>")     
    print("update <server-ID1> <server-ID2> <link-cost>")
    print("step") #send packets to nieghbors 
    print("packets")
    print("display")
    print("disable <server-id>")
    print("crash")
    print("help")
    print("exit")


#read Init file  
def initServer(filePath, timeInterval):
    with open(filePath, 'r') as file:
        data = json.load(file)
    
    my_id = data['server_id']
    global my_info 
    server_ids = data["server_ids"]
    for server_id in server_ids:
        if server_id['server_id'] is my_id:
            my_info = list(server_id.values())
            break
    print("my info", my_info)
    global server_thread
    server_thread = Thread(target = serverThread,args=(my_info), daemon=True )
    server_thread.start()



def serverThread(sid, ip, port):
    print(sid, ip, port )
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((ip, port))
        server_socket.listen()         

def updateEdge():
    print("updating edge")


def step():
    print("sending packets to the neighbors")

def displayPackets():
    print("you've received this many packets")

def displayRoutingTable():
    print(TOPOLOGY_TABLE)

def disableServer(serverID):
    print(f"we'll shutdown server {serverID}")

def simulateCrash():
    print("simulating a crash")

def processInput(user_input):
    input_arr = user_input.split()
    if input_arr[0] == "init":
        initServer(input_arr[2], input_arr[4])
        print("finished init")
    elif input_arr[0] == "update":
        updateEdge()
    elif input_arr[0] == "step":
        step()
    elif input_arr[0] == "packets":
        displayPackets()
    elif input_arr[0] == "display":
        displayRoutingTable()
    elif input_arr[0] == "disable":
        disableServer(input_arr[1])
    elif input_arr[0] == "crash":
        simulateCrash()
    elif input_arr[0] == "help":
        showPrompt()
    elif input_arr[0] == "exit" or input_arr[0] =="q":
        exit()



if __name__ == '__main__':
    #display server options
    showPrompt()

    #run main loop
    while True:
        user_input = input("make selection:")
        processInput(user_input)
    