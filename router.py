



def showPrompt():
    print("server -t <file-name> -i <interval>")     
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
    print("initializing router table")
    print("from init method", filePath)
    print("from init method", timeInterval)

    #broadcast update 
def updateEdge():
    print("updating edge")


def step():
    print("sending packets to the neighbors")

def displayPackets():
    print("you've received this many packets")

def displayRoutingTable():
    print("here are all the routes i got")

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
        if input_arr[0] == "server":
            initServer(input_arr[2], input_arr[4])
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


