import json
import argparse


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


#read Init file  
def initServer(filePath, timeInterval):
    with open(filePath, 'r') as file:
        initObj = json.load(file)
        file.close()
    print(json.dumps(initObj))
    print(type(initObj))
    initObj.update({"time_interval": timeInterval})
    print(initObj)

    #broadcast update 
def updateEdge():
    print("updating edge" )



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t")
    parser.add_argument("-i")
    args = parser.parse_args()

    init_file = args.t
    update_interval = args.i

    if init_file:
        initServer(init_file, 30)
    elif init_file and update_interval:
        initServer( init_file,update_interval )

    showPrompt()
    #run main loop
    while True:
        #display server options
        user_input = input("make selection:")
        input_arr = user_input.split()
        if input_arr[0] == "init":
            # initServer(input_arr[2], input_arr[4])
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


