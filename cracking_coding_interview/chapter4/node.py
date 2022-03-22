class Node:
    def __init__(self,id,name,children,state) -> None:
        self._name       = name
        self._children   = children
        self._state      = state
        self._id         = id

    def set_name(self,name):
        self._name = name
    def set_children(self,children):
        self._children = children

    def get_name(self):
        return self._name
    def get_child(self):
        return self._children  

    def set_state(self,state):
        self._state = state
    def get_state(self):
        return self._state
    def set_id(self,id):
        self._id = id
    def get_id(self):
        return self._id
    def __eq__(self, __o: object) -> bool:
        return self._id == __o._id    

