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

def stringToTupple(string):
    tuple = string.split(" ")
    for i in range(len(tuple)):
        tuple[i] = int(tuple[i])
    return tuple
    
def generateTopologyDict(lines):
    l = len(lines)
    topologyDict = {
        "server_id": lines[0].strip(),
        "total_servers": lines[1].strip(),
        "edge_nums":lines[2].strip(),
        "topology_info":[],
        "known_routes":[]
    }

    for i in range(3,6):
        topologyDict['topology_info'].append(lines[i].strip())
    for i in range(7, l):
        topologyDict['known_routes'].append(stringToTupple(lines[i].strip()))

    return topologyDict 

#read Init file  
def initServer(filePath, timeInterval):
    fileLineArray = []
    print("from init method", filePath)
    print("from init method", timeInterval)
    print("initializing router table")
    with open(filePath , 'r') as file:
        lines = file.readlines()

    global TOPOLOGY_TABLE
    TOPOLOGY_TABLE = generateTopologyDict(lines)
    print(TOPOLOGY_TABLE)
    
    #broadcast update 
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






if __name__ == '__main__':
    
    showPrompt()
    #run main loop
    while True:
        #display server options
        user_input = input("make selection:")
        input_arr = user_input.split()
        if input_arr[0] == "init":
            initServer(input_arr[2], input_arr[4])
            print()
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
        elif input_arr[0] == "exit":
            exit(1)