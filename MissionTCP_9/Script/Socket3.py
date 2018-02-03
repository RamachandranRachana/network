import socket
import pickle
import time
from Conn import Connect
def shortestpathAnnJan(graph,start,end,visited=[],distances={},predecessors={}):
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
    # process neighbors as per algorithm, keep trackno of predecessors
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
    return shortestpathAnnJan(graph,closestnode,end,visited,distances,predecessors)

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
    # process neighbors as per algorithm, keep trackno of predecessors
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

def shortestpathJanChan(graph,start,end,visited=[],distances={},predecessors={}):
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
    # process neighbors as per algorithm, keep trackno of predecessors
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
    return shortestpathJanChan(graph,closestnode,end,visited,distances,predecessors)

class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """
    def mysend(self,msg,host,port):
        self.sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock1.connect((host,port))
        data_string = pickle.dumps(msg)
        self.sock1.send(data_string)
        self.sock1.close
        if msg['drp']==1:
            msg['drp']=0
            the_time = time.time()
            start_time = the_time
            end_time = the_time + 5  # 24 hrs
            while the_time < end_time:
                print('Did not recieve acknowledgement yet')
                time.sleep(1)  # wait 60 seconds
                the_time = time.time()  # get the new time

            self.sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock2.connect((host, port))
            data_string = pickle.dumps(msg)
            self.sock2.send(data_string)
        if msg['fin']==1:
            print ("Ending Mission")
    def killchan(self):
        pack = {'src': 'Ann', 'dest': 'Chan', 'i': 1,'data':'Terminate Chan', 'syn': 0,'urg':0,'ack': 0, 'seqno': 1, 'ackno': 0, 'headerlenght': 20,
                'checksum': 10001010, 'drp': 0,'rst':1,'ter':1,'fin':0}
        co = open("chan.txt", "r+")
        strbuff=co.read()
        co.close()
        print (strbuff)
        self.killchan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.killchan.connect(('127.0.0.4', 200))
        data_string = pickle.dumps(pack)
        self.killchan.send(data_string)



    def __init__(self,flag='c',host='127.0.0.2',shost='127.0.0.1',sport=127,port=101,sock=None,):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            graph = {'Ann': {'A': 0},
                 'A': {'Ann': 0, 'B': 4, 'C': 3, 'E': 7},
                 'B': {'A': 4, 'C': 6, 'L': 5},
                 'C': {'A': 3, 'B': 6, 'D': 11},
                 'Chan': {'E': 0},
                 'E': {'Chan': 0, 'A': 7, 'G': 5},
                 'L': {'B': 5, 'D': 9, 'F': 5},
                 'D': {'L': 9, 'F': 6, 'G': 10, 'C': 11},
                 'G': {'E': 5, 'D': 10},
                 'Jan': {'F': 0,'H':0},
                 'H':{'Jan':0},
                 'F': {'Jan': 0, 'L': 5, 'D': 6}}
            self.pathaj = shortestpathAnnJan(graph,'Ann','Jan')
            self.pathac = shortestpathAnnChan(graph,'Ann','Chan')
            self.pathjc = shortestpathJanChan(graph,'Jan','Chan')
            self.pathja = []
            self.pathca = []
            self.pathcj = []
            self.pathjh=['Jan','H']
            self.pathhj=['H','Jan']
            for i in range(len(self.pathaj) - 1, -1, -1):
                self.pathja.append(self.pathaj[i])
            for i in range(len(self.pathac) - 1, -1, -1):
                self.pathca.append(self.pathac[i])
            for i in range(len(self.pathjc) - 1, -1, -1):
                self.pathcj.append(self.pathjc[i])

        else:
            self.sock = sock
        if flag=='l':
            self.sock.bind((host, port))
            countChan = 0
            countJan = 0
            self.sock.listen(5)                # Now wait for client connection.
            while True:
                c, addr = self.sock.accept()     # Establish connection with client.
                print ('Got connection from',addr)
                data=c.recv(1024)
                data_arr= pickle.loads(data)
                print (data_arr)
                self.sock.close
                if data_arr['src']=='H' and data_arr['dest']=='Jan':
                    if data_arr['data']=='CONGRADS MISSION ACCOMPLISHED':
                        data_arr['data']='CONGRATULATIONS WE FRIED DRY GREEN LEAVES'
                        data_arr['src']='Jan'
                        data_arr['dest']='Ann'
                        path=self.pathja
                        data_arr['urg']=1
                        data_arr['syn'] = 0
                        data_arr['ackno'] = data_arr['seqno'] + 1
                        data_arr['ack'] = 1
                        data_arr['seqno'] =1


                elif data_arr['src']=='Ann' and data_arr['syn']==1 and data_arr['ackno']==2:
                    #acknonowledge recieved from Ann
                    data_arr['ackno']=2
                    data_arr['syn']=0
                    if data_arr['dest']=='Chan':
                        data_arr['src']='Chan'
                        data_arr['dest']='Ann'
                        path =self.pathca
                    else:
                        data_arr['src'] = 'Jan'
                        data_arr['dest'] = 'Ann'
                        path = self.pathja
                elif data_arr['src']=='Ann' and data_arr['syn']==0 and data_arr['seqno']!=0:
                    print (data_arr['data'])
                    if data_arr['ter']==1 and data_arr['rst']==1:
                        self.sock.shutdown(1)
                    if data_arr['dest'] == 'Chan':
                        co = open("chan.txt", "a")
                        co.write("Data from ann to chan :"+ "\n");
                        co.write(data_arr['data']+ "\n")
                        co.close()
                    else:
                        jo = open("jan.txt", "a")
                        jo.write("Data from ann to jan :"+ "\n");
                        jo.write(data_arr['data']+ "\n")
                        jo.close()
                    # Close opend file
                    if data_arr['data']=='Execute:PEPPER THE PEPPER':
                        path=self.pathjh
                        data_arr['urg']=1
                        data_arr['data']='PEPPER THE PEPPER'
                        data_arr['src']='Jan'
                        data_arr['dest']='H'
                        data_arr['i']=1
                        data_arr['seqno']=1
                        data_arr['ackno']=1
                    elif data_arr['data']=='congrads !! Lets meet at (32.76” N, -97.07” W)':
                        path = self.pathja
                        data_arr['urg'] = 0
                        data_arr['data'] = 'OK'
                        data_arr['src'] = 'Jan'
                        data_arr['dest'] = 'Ann'
                        data_arr['i'] = 1
                        data_arr['seqno'] = 1
                        data_arr['ackno'] = 1
                        data_arr['fin']=1
                    else:
                        datas = input('Type the data for Ann:')
                        data_arr['data'] = datas

                        if data_arr['dest']=='Chan':
                            data_arr['src'] = 'Chan'
                            path = self.pathca
                            countChan = countChan + 1
                            count=countChan
                            co = open("chan.txt", "a")
                            co.write("Data from chan to aan :"+ "\n");
                            co.write(data_arr['data']+ "\n")
                            co.close()
                        else:
                            data_arr['src'] = 'Jan'
                            path = self.pathja
                            countJan=countJan+1
                            count=countJan
                            jo = open("jan.txt", "a")
                            jo.write("Data from jan to aan :"+ "\n");
                            jo.write(data_arr['data']+ "\n")
                            jo.close()
                        data_arr['dest'] = 'Ann'
                        data_arr['i'] = 1
                        data_arr['syn'] = 0
                        data_arr['ackno'] =data_arr['seqno']+1
                        data_arr['ack']=1
                        data_arr['seqno'] = count
                data_arr['i'] = 1
                j = data_arr['i']
                c = path[j]
                print
                if c == 'A':
                    host = '127.0.0.4'
                    port = 200
                if c == 'B':
                    host = '127.0.0.5'
                    port = 201
                if c == 'C':
                    host = '127.0.0.6'
                    port = 202
                if c == 'D':
                    host = '127.0.0.7'
                    port = 203
                if c == 'E':
                    host = '127.0.0.8'
                    port = 204
                if c == 'F':
                    host = '127.0.0.9'
                    port = 205
                if c == 'G':
                    host = '127.0.0.11'
                    port = 206
                if c == 'H':
                    host = '127.0.0.12'
                    port = 207
                if c == 'L':
                    host = '127.0.0.13'
                    port = 208
                if c == 'Ann':
                    host = '127.0.0.1'
                    port = 127
                if c == 'Jan':
                    host = '127.0.0.2'
                    port = 110
                if c == 'Chan':
                    host = '127.0.0.3'
                    port = 100
                self.mysend(data_arr, host, port)
        if flag=='s':
            self.sock.bind((host, port))
            countac=1
            countaj=1
            self.sock.listen(5)                 # Now wait for client connection.
            while True:
                c, addr = self.sock.accept()     # Establish connection with client.
                print ('Got connection from',addr)
                data=c.recv(1024)
                data_arr = pickle.loads(data)
                self.sock.close                   
                print (data_arr)
                if (data_arr['src']=='Chan' and data_arr['dest']=='Ann'):
                    if data_arr['syn']==0 and data_arr['seqno']!=0:
                        print(data_arr['data'])
                        ao = open("annchan.txt", "a")
                        ao.write("Data from chan to aan :" + "\n");
                        ao.write(data_arr['data'] + "\n")
                        ao.close()
                        if data_arr['seqno']==5:
                            print ('recieved 5th packet from chan')
                            print ('intrusion at chan')
                            self.killchan()
                            countaj=countaj+1
                            path=self.pathaj
                            data_arr['src'] = 'Ann'
                            data_arr['dest'] = 'Jan'
                            data_arr['i'] = 1
                            data_arr['syn'] = 0
                            data_arr['ack'] = 0
                            data_arr['ackno'] =0
                            data_arr['urg']=1
                            data_arr['data']='Intrusion at Chan! Alert'
                            data_arr['seqno'] = countaj
                            data_arr['drp'] = 0
                        else:
                            countac = countac + 1
                            datas = input('Ann type the data for Chan:')
                            data_arr['data'] = datas
                            ao = open("annchan.txt", "a")
                            ao.write("Data from aan to chan :" + "\n");
                            ao.write(data_arr['data'] + "\n")
                            ao.close()
                            path = self.pathac
                            data_arr['src'] = 'Ann'
                            data_arr['dest'] = 'Chan'
                            data_arr['i'] = 1
                            data_arr['syn'] = 0
                            data_arr['ack']=1
                            data_arr['ackno'] = data_arr['seqno'] + 1
                            data_arr['seqno'] = countac
                            data_arr['drp']=0
                            if data_arr['seqno']==5 or data_arr['seqno']==10:
                                data_arr['drp'] = 1
                    elif (data_arr['syn']==0 and data_arr['ackno']==2 and data_arr['seqno']==0):
                        #3 way handshake was established between chan and ann
                        print (" 3 way handshake between chan and ann established")
                        datas = input('Ann type the data for chan: ')
                        data_arr['data']=datas
                        ao = open("annchan.txt", "a")
                        ao.write("Data from aan to chan :" + "\n");
                        ao.write(data_arr['data'] + "\n")
                        ao.close()
                        path=self.pathac
                        data_arr['src'] = 'Ann'
                        data_arr['dest'] = 'Chan'
                        data_arr['i'] = 1
                        data_arr['syn'] = 0
                        data_arr['ack']=0
                        data_arr['ackno'] =0
                        data_arr['seqno']=1
                    else:
                        path=self.pathac
                        data_arr['src']='Ann'
                        data_arr['dest']='Chan'
                        data_arr['i']=1
                        data_arr['syn']=1
                        data_arr['ack']=1
                        data_arr['ackno']=2
                if (data_arr['src']=='Jan' and data_arr['dest']=='Ann'):
                    if data_arr['syn'] == 0 and data_arr['seqno'] != 0:
                        print(data_arr['data'])
                        ao1 = open("annjan.txt", "a")
                        ao1.write("Data from jan to aan :" + "\n");
                        ao1.write(data_arr['data'] + "\n")
                        ao1.close()
                        countaj = countaj + 1
                        if data_arr['data']=='TarAt32° 43’ 22.77” N,97° 9’ 7.53” W':
                            data_arr['data']='Execute:PEPPER THE PEPPER'
                        elif data_arr['data']=='CONGRATULATIONS WE FRIED DRY GREEN LEAVES':
                            data_arr['data']='congrads !! Lets meet at (32.76” N, -97.07” W)'
                        else:
                            datas = input('Ann type the data for Jan:')
                            data_arr['data'] = datas
                        ao1 = open("annjan.txt", "a")
                        ao1.write("Data from aan to jan :" + "\n");
                        ao1.write(data_arr['data'] + "\n")
                        ao1.close()
                        path = self.pathaj
                        data_arr['src'] = 'Ann'
                        data_arr['dest'] = 'Jan'
                        data_arr['i'] = 1
                        data_arr['syn'] = 0
                        data_arr['ackno'] = data_arr['seqno'] + 1
                        data_arr['seqno'] = countaj
                        data_arr['drp'] = 0
                        if data_arr['seqno']==5 or data_arr['seqno']==10:
                            data_arr['drp']=1
                    elif (data_arr['syn']== 0 and data_arr['ackno'] == 2 and data_arr['seqno'] == 0):
                        # 3 way handshake was established between chan and ann
                        print(" 3 way handshake between jan and ann established")
                        datas = input('Ann type the data for Jan: ')
                        data_arr['data'] = datas
                        ao1 = open("annjan.txt", "a")
                        ao1.write("Data from aan to jan :" + "\n");
                        ao1.write(data_arr['data'] + "\n")
                        ao1.close()
                        path = self.pathaj
                        data_arr['src'] = 'Ann'
                        data_arr['dest'] = 'Jan'
                        data_arr['i'] = 1
                        data_arr['syn'] = 0
                        data_arr['ack'] = 0
                        data_arr['ackno'] = 0
                        data_arr['seqno'] = countaj
                    else:
                        path=self.pathaj
                        data_arr['src']='Ann'
                        data_arr['dest']='Jan'
                        data_arr['i'] = 1
                        data_arr['syn'] = 1
                        data_arr['ack'] = 1
                        data_arr['ackno'] = 2
                j=data_arr['i']
                c=path[j]
                if c=='A':
                    host='127.0.0.4'
                    port=200
                if c=='B':
                    host='127.0.0.5'
                    port=201
                if c=='C':
                    host='127.0.0.6'
                    port=202
                if c=='D':
                    host='127.0.0.7'
                    port=203
                if c=='E':
                    host='127.0.0.8'
                    port=204
                if c=='F':
                    host='127.0.0.9'
                    port=205
                if c=='G':
                    host='127.0.0.11'
                    port=206
                if c=='H':
                    host='127.0.0.12'
                    port=207
                if c=='L':
                    host='127.0.0.13'
                    port=208
                if c=='Ann':
                    host='127.0.0.1'
                    port=127
                if c=='Jan':
                    host='127.0.0.2'
                    port=110
                if c=='Chan':
                    host='127.0.0.3'
                    port=100
                print ('sending to ' +c )
                print ('with ip'+host)
                self.mysend(data_arr,host,port)

        if flag=='r':
            self.sock.bind((host,port))
            self.sock.listen(5)
            while True:
                c,addr=self.sock.accept()
                data=c.recv(1024)
                data_arr = pickle.loads(data)
                print (data_arr)
                if data_arr['drp']==1:
                    if data_arr['urg']==1:
                        data_arr['drp']=0
                    else:
                        print ('dropping the packet')
                        continue
                if ((data_arr['src']=='Ann' and data_arr['dest']=='Chan') or (data_arr['src']=='Chan' and data_arr['dest']=='Ann')):

                    if data_arr['src']=='Chan' :
                        path=self.pathca
                    else :
                        path=self.pathac
                if ((data_arr['src']=='Jan' and data_arr['dest']=='Chan') or (data_arr['src']=='Chan' and data_arr['dest']=='Jan')):

                    if data_arr['src']=='Chan' :
                        path=self.pathaj
                    else :
                        path=self.pathja
                if ((data_arr['src']=='Ann' and data_arr['dest']=='Jan') or (data_arr['src']=='Jan' and data_arr['dest']=='Ann')):

                    if data_arr['src']=='Jan' :
                        path=self.pathja
                    else :
                        path=self.pathaj
                if (data_arr['src']=='Jan' and data_arr['dest']=='H'):
                    if data_arr['data']=='PEPPER THE PEPPER':
                        print('Target identified!!')
                        print('Eliminating Target!!')
                        print('Mission Accomplished!!')
                        path=self.pathhj
                        data_arr['src']='H'
                        data_arr['dest']='Jan'
                        data_arr['data']='CONGRADS MISSION ACCOMPLISHED'
                        data_arr['i']=0
                j=data_arr['i']
                k=j+1
                data_arr['i']=k
                c=path[k]
                print(path)
                if c=='A':
                    host='127.0.0.4'
                    port=200
                if c=='B':
                    host='127.0.0.5'
                    port=201
                if c=='C':
                    host='127.0.0.6'
                    port=202
                if c=='D':
                    host='127.0.0.7'
                    port=203
                if c=='E':
                    host='127.0.0.8'
                    port=204
                if c=='F':
                    host='127.0.0.9'
                    port=205
                if c=='G':
                    host='127.0.0.11'
                    port=206
                if c=='H':
                    host='127.0.0.12'
                    port=207
                if c=='L':
                    host='127.0.0.13'
                    port=208
                if c=='Ann':
                    host='127.0.0.1'
                    port=127
                if c=='Jan':
                    host='127.0.0.2'
                    port=110
                if c=='Chan':
                    host='127.0.0.3'
                    port=100

                print ('sending to ' +c )
                print ('with ip'+host)
                self.sock.close
                self.mysend(data_arr,host,port)
            

    def connect(self, host, port,data='HELLO'):
        self.sock.connect((host, port))
        print ('connecting to'+host)
        self.sock.send(data.encode(encoding='utf_8'))
        self.sock.close
    def connectlist(self,host,port,data={}):
        self.sock.connect((host, port))        
        data_string = pickle.dumps(data)
        self.sock.send(data_string)
        self.sock.close          


