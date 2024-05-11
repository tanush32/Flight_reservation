class node:
    def __init__(self,state):
        self.state=state
        self.flight={}
        self.right=None
        self.left=None
        

class flight_info:
    def __init__(self):
        self.root=None

    def insert_state(self,state):
        if self.root is None:
            self.root = node(state)  
        else:

            n=node(state)    
            cur = self.root
            while cur.right:
                cur = cur.right 
            cur.right = n
            n.left = cur   
            n.right = None

    def insert_flight(self, state, name, path, a_time, d_time, unit_price):
        if len(path) == 0:
            return 
        
        # Find the node for the current state
        cur = self.root
        while cur:
            if cur.state == state:
                if len(path) >= 2:
                     # Store flight information for the first state in the path
                    cur.flight[name]={}
                    cur.flight[name]["path"] = path
                    cur.flight[name]["a_time"] = a_time
                    cur.flight[name]["d_time"] = d_time
                    cur.flight[name]["unit_price"] = unit_price
                break
            cur = cur.right
        
        # Recursive call for next state in the path
        if len(path) > 2:
            self.insert_flight(path[1], name, path[1:], a_time[1:], a_time[1], unit_price)

    def display(self):
        cur = self.root
        while cur:
            print(cur.state, cur.flight)   
            print() 
            cur = cur.right



flight = flight_info()
flight.insert_state("s1")
flight.insert_state("s2")
flight.insert_state("s3")
flight.insert_flight("s1","King_fisher",["s1","s2","s3"],[2,3],1,200)
flight.insert_flight("s1","Queen_fisher",["s1","s3","s2"],[3,4],1,400)
flight.display()
            

                











class graph :
    def __init__(self,verts):
        self.verts=verts
        self.graph=[[float('inf') for i in range(verts)] for j in range(verts)]

    def size(self):
        return self.verts
        
    def display(self):
        for i in self.graph:
            print(i)

    def add_edges(self,vertex1,vertex2):
        print("Add edge ",vertex1," to ",vertex2)
        #i = int(input("enter the edge length : "))
        i=int(input("enter the weight :"))
        self.graph[vertex1][vertex2]=i
        self.graph[vertex2][vertex1]=i

    def add_vertex(self):
        self.verts+=1
        for i in range(self.verts-1):
            self.graph[i].append(0)
        self.graph.append([0 for i in range(self.verts)]) 

    
