import Tree
class BinaryTre(Tree):
    def left(self,p):
        raise NotImplementedError
    def right(self,p):
        raise NotImplementedError
    
    
    def sibling(self,p):
        if self.is_root(p):
            return None
        parent = self.get_parent(p)
        if p == self.right(parent):
            return self.left(parent)
        else:
            return self.right(parent)
    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)      