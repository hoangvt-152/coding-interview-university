class Tree:
    class  Position:
        def element(self):
            raise NotImplementedError
        
        def __eq__(self, other) -> bool:
            return self == other
        
        def __ne__(self, other):
            return not self == other

    def root(self):
        raise NotImplementedError
    
    def parent(self,p):
        raise NotImplementedError
    
    def num_children(self,p):
        raise NotImplementedError
    
    def children(self,p):
        raise NotImplementedError
    
    def __len__(self):
        raise NotImplementedError
    