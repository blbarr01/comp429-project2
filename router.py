from copy import deepcopy
import json
import socket
from threading import Thread
from sys import maxsize

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
    edges = data["edges"]

    global ROUTING_TABLE 
    ROUTING_TABLE = generateRoutingTable(edges)

    # get the info for the local machine
    my_id = data['server_id']
    print("my id ", my_id)
    server_info = extractServerInfo(my_id, server_topology)
    
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
def updateTable(data):
    print(data)

def updateEdge():
    print("updating edge")

def extractServerInfo(my_id, server_topology):
    for server_id in server_topology:
        if server_id['server_id'] is my_id:
            server_info = list(server_id.values())
            return server_info 

def generateRoutingTable(edges): 
    print("edges:", edges)
    n = TOPOLOGY_TABLE["num_servers"]
    sid = TOPOLOGY_TABLE['server_id']
    routing_table = {f"{i+1}": maxsize for i in range(n)}
    routing_table.update({f"{sid}":0})
    print("routing table:", routing_table)

    for edge in edges:
        dest = edge['dest']
        routing_table[f'{dest}'] = edge['cost']

    print("routing table:", routing_table)
    return routing_table

    
    

def step():
    #for each server in our topology, send 
    server_topology
    for server in server_topology:
        if server['server_id'] is TOPOLOGY_TABLE["server_id"]:
            continue
        print(server)
        sendPacket(server)
        

def sendPacket(dest):
    packet = deepcopy(ROUTING_TABLE)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        endpoint = dictionayToTuple(dest)
        # we'll need to send the routes here we need to convert this into a byte stream
        network_packet = json.dumps(packet).encode()
        client_socket.sendto(network_packet, endpoint)
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
    elif input_arr[0] =="q1":
        initServer("./initFiles/server1.json", 30)
    elif input_arr[0] =="q2":
        initServer("./initFiles/server2.json", 30)
    elif input_arr[0] =="q3":
        initServer("./initFiles/server3.json", 30)
    elif input_arr[0] =="q4":
        initServer("./initFiles/server4.json", 30)
    elif input_arr[0] == "exit" or input_arr[0] =="e":
        exit()




if __name__ == '__main__':
    #display server options
    showPrompt()

    #run main loop
    while True:
        user_input = input("make selection:")
        processInput(user_input)
    