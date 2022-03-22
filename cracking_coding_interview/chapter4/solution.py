#4.1.RouteBetween2Nodes
from queue import Queue
from typing import List
from graph import Graph
import enum

class State(enum.Enum):
    Unvisited = 'unvisited'
    Visited   = 'visited'
    Visiting = 'visiting'

class TreeNode:
    def __init__(self,value,left=None,right=None) -> None:
        self._left  = left
        self._right = right
        self._value = value
    def set_left(self,left):
        self._left = left
    def set_right(self,right):
        self._right = right        


def route_between_two_nodes(g,start,end):
    if start == end:
        return True
    for n in g.get_nodes:
        n.set_state(State.Unvisited)
    q=Queue()
    q.put(start)
    start.set_state(State.Visiting)
    while  not q.empty():
        u = q.pop()
        if u:
            for n in u.get_children():
                if n.get_state()!=State.Visited:
                    if n == end:
                        return True
                    else:
                        u.set_state(State.Visiting)
                        q.put(u)
        u.set_state(State.Visited)
    return False


def createMinHeightBST(arr,start,end):
    if end < start:
        return None
    mid = int((start + end)/2)
    root = TreeNode(arr[mid])
    root.set_left(createMinHeightBST(arr,start,mid))
    root.set_right(createMinHeightBST(arr,mid+1,end))



def createMinHeightBST(arr):
    return createMinHeightBST(arr,0,len(arr) -1)



#4.3 List of Depths

def create_level_linked_list(root,lists,level):
    if root == None:
        return  None
    rest = None
    if len(rest) == level:
           rest = List()
           lists.append(rest)
    else:
        rest = lists[level]
    
    rest.append(root)
    create_level_linked_list(root._left,lists,level+1)
    create_level_linked_list(root._right,lists,level+1)

def create_level_linked_list(root):
    root = List()
    create_level_linked_list(root,root,0)





        




    
