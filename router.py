import json
import socket
from threading import Thread

SERVER_THREAD = None
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
def initServer(file_path, time_interval):
    #open up the json object and read it into the program 
    #assign it to a global for access 
    with open(file_path, 'r') as file:
        data = json.load(file)
    global TOPOLOGY_TABLE
    TOPOLOGY_TABLE = data

    # pull out the server topology
    global server_topology 
    server_topology = data["server_ids"]

    # get the info for the local machine
    my_id = data['server_id']
    server_info = extractServerInfo(my_id, server_topology)
    
    #prints to see
    print("server info ", server_info)
    print("server_topology", server_topology)

    #start the thread for the server to listen on 
    global SERVER_THREAD
    SERVER_THREAD = Thread(target = serverThread,args=(server_info), daemon=True )
    SERVER_THREAD.start()



def serverThread(sid, ip, port):
    print(sid, ip, port )
    # open a server socket to listen for incoming packets
    #recvfrom blocks till it gets something
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((ip, port))
        while True:
            data, addr = server_socket.recvfrom(1024)
            if data: 
                updateTable(data)   

#here we run the distance vector protocol        
def updateTable():
    print()

def updateEdge():
    print("updating edge")

def extractServerInfo(my_id, server_topology):
    for server_id in server_topology:
        if server_id['server_id'] is my_id:
            server_info = list(server_id.values())
            return server_info 



def step():
    #format the routing table into a message we want to send 
    #for each server in our topology
    server_topology
    for server in server_topology:
        if server['server_id'] is TOPOLOGY_TABLE["server_id"]:
            continue
        sendPacket(server)
        

def sendPacket(dest):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        endpoint = dictionayToTuple(dest)
        print(endpoint)
        # we'll need to send the routes here we need to convert this into a byte stream
        update_packet = ''
        client_socket.sendto(update_packet, endpoint)
    client_socket.close()
def displayPackets():
    print("you've received this many packets")

def displayRoutingTable():
    print(TOPOLOGY_TABLE)

def dictionayToTuple(dest):
    return(dest['server_ip'], dest['port'])

def disableServer(serverID):
    print(f"we'll shutdown server {serverID}")

def simulateCrash():
    print("simulating a crash")
    #loop through the list of available connections
        #open up a client for each
        #send all neihbors a special packet with edge costs of infinty 
        #  

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
    elif input_arr[0] == "quick":
        initServer("./initFiles/server1.json", 30)
    elif input_arr[0] == "exit" or input_arr[0] =="q":
        exit()



if __name__ == '__main__':
    #display server options
    showPrompt()

    #run main loop
    while True:
        user_input = input("make selection:")
        processInput(user_input)
    