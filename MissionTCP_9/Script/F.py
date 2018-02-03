from Socket3 import MySocket
class Host:
    'Common base class for all host'
    hostCount=0
    def _init_(self,name):
        self.name=name
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
    def _init_(self,name):
        self.name=name
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

F=Router()
F._init_("F")
F.startRouter()

