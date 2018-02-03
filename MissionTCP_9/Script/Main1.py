from Socket3 import MySocket
class Host:
    'Common base class for all host'
    hostCount=0
    def _init_(self,name):
        self.name=name
        Host.hostCount+=1
    def displayHost(self):
        print ("Name:",self.name,"Count:",Host.hostCount)
    def startServerSocket(self):
            if self.name=='Ann':
                    self.sa=MySocket(flag='s',host='127.0.0.1',port=127)
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

Ann=Host()
Ann._init_("Ann")
print ('Ann is running')
Ann.startServerSocket()
