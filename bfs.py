class node:
    def __init__(self, pt):
        self.position=pt
        self.parent=None
        self.left=None
        self.right=None
        self.up=None
        self.down=None

#creating nodes
_00=node((0,0));    _01=node((0,1));   _02=node((0,2))
_10=node((1,0));    _11=node((1,1));   _12=node((1,2))
_20=node((2,0));    _21=node((2,1));   _22=node((2,2))
_30=node((3,0));    _31=node((3,1));   _32=node((3,2))

grid=[_00,_01,_02,_10,_11,_12,_20,_21,_22,_30,_31,_32]

#connecting nodes
_00.right=_01;  _00.up   =_10
# _01.parent=_10.parent=_00
_01.left =_00;  _01.right=_02
# _00.parent=_02.parent=_01
_02.left =_01;  _02.up   =_12
# _01.parent=_12.parent=_02

_10.right=_11; _10.up=_20; _10.down=_00
# _11.parent=_20.parent=_00.parent=_10
_11.left=_10; _11.up=_21
# _10.parent=_21.parent=_11
_12.up=_22; _12.down=_02
# _22.parent=_02.parent=_12

_20.up=_30; _20.down=_10
# _30.parent=_10.parent=_20
_21.down=_11
# _11.parent=_21
_22.up=_32; _22.down=_12
# _32.parent=_12.parent=_22

_30.right=_31; _30.down=_20
# _31.parent=_20.pdown=_30
_31.left=_30; _31.right=_32
# _30.parent=_32.parent=_31
_32.left=_31; _32.down=_22
# _31.parent=_22.parent=_32
# tree is ready
visited=[]
queue = [] 
path=[]
# Mark the source node (starting node) as visited and enqueue it 
s=_00
queue.append(s) 
visited.append(s)
while queue: 
    s = queue.pop(0)   # pops the oldest element out
    # print (s.position, end = " ") 
    availableDirections=[]
    # print("Available Directions ",end=' ')
    if s.left!=None:
        if s.left!=s.parent:
            availableDirections.append(s.left)
            s.left.parent=s
            # print("left",end=' ')
    if s.right!=None:
        if s.right!=s.parent:
            availableDirections.append(s.right)
            s.right.parent=s
            # print("right",end=' ')
    if s.up!=None:
        if s.up!=s.parent:
            availableDirections.append(s.up)
            s.up.parent=s
            # print("up",end=' ')
    if s.down!=None:
        if s.down!=s.parent:
            availableDirections.append(s.down)
            s.down.parent=s
            # print("down",end=' ')
    # print()
    if s==_21: # Goal is reached
        break
    for i in availableDirections: 
        if not i in visited: 
            queue.append(i) 
            visited.append(i)
        # print(queue[0])
while(s):
    path.append(s.position)
    s=s.parent
path.reverse()
print(path) # Final Path