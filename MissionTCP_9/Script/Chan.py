import socket
from Socket3 import MySocket

def connectionSetup(src,dst,Path):
	for i in range(1,len(Path)-1):
		if Path[i]=='A':
			A.routingTable(src,dst,Path[i-1],Path[i+1])
		if Path[i]=='B':
			B.routingTable(src,dst,Path[i-1],Path[i+1])
		if Path[i]=='C':
			C.routingTable(src,dst,Path[i-1],Path[i+1])
		if Path[i]=='D':
			D.routingTable(src,dst,Path[i-1],Path[i+1])
		if Path[i]=='E':
			E.routingTable(src,dst,Path[i-1],Path[i+1])
		if Path[i]=='F':
			F.routingTable(src,dst,Path[i-1],Path[i+1])
		if Path[i]=='L':
			L.routingTable(src,dst,Path[i-1],Path[i+1])
		if Path[i]=='G':
			G.routingTable(src,dst,Path[i-1],Path[i+1])
			
def shortestpathAnnChan(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path between start and end nodes in a graph"""
    # we've found our end node, now find the path to it, and return
    if start==end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return path[::-1]
    # detect if it's the first time through, set current distance to zero
    if not visited: distances[start]=0
    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,999)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start
    # neighbors processed, now mark the current node as visited
    visited.append(start)
    # finds the closest unvisited node to the start
    unvisiteds = dict((k, distances.get(k,999)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    # now we can take the closest node and recurse, making it current
    return shortestpathAnnChan(graph,closestnode,end,visited,distances,predecessors)

class Host:
    'Common base class for all host'
    hostCount=0
    def _init_(self,name,ip,port):
        self.name=name
        self.ip=ip
        self.port=port
        Host.hostCount+=1
    def displayHost(self):
        print ("Name:",self.name,"Count:",Host.hostCount)
    def startServerSocket(self):
            if self.name=='Ann':
                    self.sa=MySocket(flag='s',host='127.0.0.1',port=111)
            if self.name=='Jan':
                    self.sa=MySocket(flag='s',host='127.0.0.2',port=110)
            if self.name=='Chan':
                    self.sa=MySocket(flag='s',host='127.0.0.3',port=100)
    def startServerListener(self):
            if self.name=='Ann':
                    self.sa=MySocket(flag='l',host='127.0.0.1',port=111)
            if self.name=='Jan':
                    self.sa=MySocket(flag='l',host='127.0.0.2',port=110)
            if self.name=='Chan':
                    self.sa=MySocket(flag='l',host='127.0.0.3',port=100)
    def createClientSocket(self,host,port,pack={}):
        self.sa=MySocket()
        self.sa.connectlist(host,port,pack)
                       

class Router:
    'Common base class for all router'
    routerCount=0
    def _init_(self,name,ip,port):
        self.name=name
        self.ip=ip
        self.port=port
        self.rt=[["src","dst","innode","outnode"]]
        Router.routerCount+=1
    def displayRouter(self):
        print ("Name:",self.name,"Count:",Router.routerCount)
    def routingTable(self,src,dst,a,b):
	    tup=[src,dst,a,b]
	    self.rt.append(tup)
    def printRoutingTable(self):
        for i in range(0,len(self.rt)):
            print (self.rt[i])

#Initialize the network routers & Hosts
Ann=Host()
Ann._init_("Ann",'127.0.0.1',127)
Jan=Host()
Jan._init_("Jan",'127.0.0.2',110)
Chan=Host()
Chan._init_("Chan",'127.0.0.3',100)
A=Router()
A._init_("A",'127.0.0.4',200)
B=Router()
B._init_("B",'127.0.0.5',201)
C=Router()
C._init_("C",'127.0.0.6',202)
D=Router()
D._init_("D",'127.0.0.7',203)
E=Router()
E._init_("E",'127.0.0.8',204)
F=Router()
F._init_("F",'127.0.0.9',205)
G=Router()
G._init_("G",'127.0.0.11',206)
H=Router()
H._init_("H",'127.0.0.12',207)
L=Router()
L._init_("L",'127.0.0.13',208)

#Network topology and determining path from chan to ann
graph={Ann.name : {A.name : 0},
        A.name : {Ann.name : 0,B.name : 4,C.name : 3,E.name : 7},
        B.name : {A.name : 4,C.name : 6,L.name : 5},
        C.name : {A.name : 3,B.name : 6,D.name : 11},
        Chan.name : {E.name : 0},
        E.name : {Chan.name : 0,A.name : 7,G.name : 5},
        L.name : {B.name : 5,D.name : 9,F.name : 5},
        D.name : {L.name : 9,F.name : 6,G.name : 10,C.name : 11},
        G.name : {E.name : 5,D.name : 10},
        Jan.name : {F.name : 0},
        F.name : {Jan.name : 0,L.name : 5,D.name : 6}}

pathac=shortestpathAnnChan(graph,Ann.name,Chan.name)
pathca=[]
for i in range(len(pathac)-1,-1,-1):
    pathca.append(pathac[i])
connectionSetup(Chan.name,Ann.name,pathca)


#Starting the client socket for chan           
pack={'src': 'Chan','dest':'Ann','i':1,'syn':1,'ack':0,'seqno':0,'ackno':0,'headerlenght':20,'checksum':10001010,'drp':0,'ter':0,'rst':0,'fin':0,'urg':0}
j=pack['i']
c=pathca[j]
#Determine host and port of next router
if c=='A':
    host=A.ip
    port=A.port
if c=='B':
    host=B.ip
    port=B.port
if c=='C':
    host=C.ip
    port=C.port
if c=='D':
    host=D.ip
    port=D.port
if c=='E':
    host=E.ip
    port=E.port
if c=='F':
    host=F.ip
    port=F.port
if c=='G':
    host=G.ip
    port=G.port
if c=='L':
    host=L.ip
    port=L.port
print('Chan is up and running')
print ('Chan is establishing a communicatin with Ann')
#Start commununication from Chan to Ann
Chan.createClientSocket(host,port,pack)
Chan.startServerListener()

