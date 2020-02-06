class node:
    def __init__(self, pt):
        self.position=pt
        self.left=None
        self.right=None
        self.up=None
        self.down=None

_00=node((0,0));    _01=node((0,1));   _02=node((0,2))
_10=node((1,0));    _11=node((1,1));   _12=node((1,2))
_20=node((2,0));    _21=node((2,1));   _22=node((2,2))
_30=node((3,0));    _31=node((3,1));   _32=node((3,2))

_00.right=_01;  _00.up   =_10
_01.left =_00;  _01.right=_02
_02.left =_01;  _02.up   =_12

_10.right=_11; _10.up=_20; _10.down=_00
_11.left=_10
_12.up=_22; _12.down=_02

_20.up=_30; _20.down=_10
_21.down=_11
_22.up=_32; _22.down=_12

_30.right=_31; _30.down=_20
_31.left=_30; _31.right=_32
_32.left=_31; _32.down=_22
# tree is ready
visited=[]
def BFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print (s, end = " ") 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True