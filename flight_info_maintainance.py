class compartment_node:
    def __init__(self,name):
        self.compartment_name=name
        self.aisle=1
        self.window=1
        self.middle=1
        self.next=None

    
class compartment_list:
    def __init__(self):
        self.head=None
    def generate_compartment(self,no_of_compartments):
        while no_of_compartments>0:
            x=65
            compartment=compartment_node(chr(x))
            if self.head is None:
                self.head=compartment
            else:
                current_compartment=self.head
                while(current_compartment.next):
                    current_compartment=current_compartment.next
                current_compartment.next=compartment
            x=x+1
            no_of_compartments=no_of_compartments-1

    def seat_booking(self):
        self.display_compartment_availability()
        print()
        print("Select the seat you want to book : ")
        print()
        


    def display_compartment_availability(self):
        cur = self.head
        while cur :
            print(cur.compartment_name)
            print(" aisle - ",cur.aisle," Window - ",cur.window,"Middle - ",cur.middle)
            print("--------------------------------------------------------------------")
            cur=cur.next
        print()    



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

    def insert_flight(self, state, name, path, a_time, d_time, unit_price,no_of_compartments):
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
                    compartment=compartment_list()
                    compartment.generate_compartment(no_of_compartments)
                    cur.flight[name]["no_of_compartments"]=compartment.head
                break
            cur = cur.right
        
        # Recursive call for next state in the path
        if len(path) > 2:
            self.insert_flight(path[1], name, path[1:], a_time[1:], a_time[1], unit_price,no_of_compartments)



    def display(self):
        cur = self.root
        while cur:
            print(cur.state, cur.flight)   
            print() 
            cur = cur.right

    def find_fastest(self, start, end, obj):
        cur = self.root
        min_time = float('inf')
        fastest_flight = None

        while cur:
            if cur.state == start:
                for flight_name, details in cur.flight.items():
                    if end in details["path"]:
                        total_time = 0
                        path = details["path"]
                        path_length = len(path)

                        for i in range(path_length - 1):
                            # Add travel time between states
                            total_time += obj.graph[path[i]][path[i + 1]]
                            if path[i + 1] == end:
                                break

                        if total_time < min_time:
                            min_time = total_time
                            fastest_flight = flight_name
            cur = cur.right

        return fastest_flight
                                




class graph :
    def __init__(self,verts):
        self.verts=verts
        self.graph=[[float('inf') for i in range(verts)] for j in range(verts)]

    def size(self):
        return self.verts
    
    #displaying the distance info     
    def display(self):
        for i in self.graph:
            print(i)

    #updating the distance between two states
    def add_edges(self,vertex1,vertex2,weight):
        print("Add edge ",vertex1," to ",vertex2)
        self.graph[vertex1][vertex2]=weight
        self.graph[vertex2][vertex1]=weight

    #addind state
    def add_vertex(self):
        self.verts+=1
        for i in range(self.verts-1):
            self.graph[i].append(0)
        self.graph.append([0 for i in range(self.verts)]) 


#graph initalization   
g=graph(3)
g.add_edges(0,1,4)
g.add_edges(1,2,6)
g.add_edges(2,0,11)


#flight info initialization  
flight = flight_info()
flight.insert_state(0)
flight.insert_state(1)
flight.insert_state(2)
flight.insert_flight(0,"King_fisher",[0,1,2],[2,3],1,200,5)
flight.insert_flight(0,"Queen_fisher",[0,2,1],[3,4],1,400,4)
flight.display()
print(flight.find_fastest(0,2,g))
