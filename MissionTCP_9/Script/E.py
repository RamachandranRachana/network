from Socket3 import MySocket
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
    def createServerSocket(self):
            if self.name=='Ann':
                    self.sa=MySocket(flag='s',host='127.0.0.1',port=111)
            if self.name=='Jan':
                    self.sa=MySocket(flag='s',host='127.0.0.2',port=110)
            if self.name=='Chan':
                    self.sa=MySocket(flag='s',host='127.0.0.3',port=100)
                    

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
    def startRouter(self):
        if self.name=='A':
            self.sr=MySocket(flag='r',host='127.0.0.4',port=200)
        if self.name=='B':
            self.sr=MySocket(flag='r',host='127.0.0.5',port=201)
        if self.name=='C':
            self.sr=MySocket(flag='r',host='127.0.0.6',port=202)
        if self.name=='D':
            self.sr=MySocket(flag='r',host='127.0.0.7',port=203)
        if self.name=='E':
            self.sr=MySocket(flag='r',host='127.0.0.8',port=204)
        if self.name=='F':
            self.sr=MySocket(flag='r',host='127.0.0.9',port=205)
        if self.name=='G':
            self.sr=MySocket(flag='r',host='127.0.0.11',port=206)
        if self.name=='H':
            self.sr=MySocket(flag='r',host='127.0.0.12',port=207)
        if self.name=='L':
            self.sr=MySocket(flag='r',host='127.0.0.13',port=208)

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


#Starting router E
E.startRouter()

