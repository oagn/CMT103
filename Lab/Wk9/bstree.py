'''Binary Search Tree In-Class and Lab Incomplete Version '''

class BTNode(object):
    def __init__(self, _element=None, _parent=None, _leftchild=None, _rightchild=None):
        self.element =_element
        self.parent = _parent
        self.leftchild = _leftchild
        self.rightchild = _rightchild
        
    @property
    def isroot(self):
        return self.parent==None

    @property
    def isleaf(self):
        return self.leftchild==None and self.rightchild==None

    @property
    def hasleftchild(self):
        return not self.leftchild==None

    @property
    def hasrightchild(self):
        return not self.rightchild==None

    def __str__(self):
        parent = 'None' if self.parent==None else str(self.parent.element)
        lchild = 'None' if self.leftchild==None else str(self.leftchild.element)
        rchild = 'None' if self.rightchild==None else str(self.rightchild.element)
        return "BTNode <'("+str(self.element)+", "+parent+", "+lchild+", "+rchild+")'>"


        
class BSTree(object):
    def __init__(self):
        self.root=None
        self.size=0

    def __add(self, subroot, e):
        '''private recursive add(subroot, e): add a new node with
        element e to the subtree rooted at subroot'''
        if subroot.element >e:
            if subroot.hasleftchild:
                self.__add(subroot.leftchild, e)
            else:
                subroot.leftchild = BTNode(e, subroot)
        else:
            if subroot.hasrightchild:
                self.__add(subroot.rightchild, e)
            else:
                subroot.rightchild = BTNode(e, subroot)
        self.size+=1

                
    def add(self, e):
        '''recursive add(subroot, e): adds a new node with
        element e to the bstree'''
        if self.size==0:
            self.root = BTNode(e)
            self.size=1
            return
        self.__add(self.root, e)

    
    def __strR(self, subroot):
        '''private recursive method to be called by __str__().
        it returns a string representation of the subtree rooted at subroot'''
        if subroot==None: return "()"
        elif subroot.isleaf: return "("+str(subroot.element)+")"
        else:
            return "("+str(subroot.element)+", "+ self.__strR(subroot.leftchild)+", "+self.__strR(subroot.rightchild)+")"
        
    def __str__(self):
        '''returns the string presentation of the tree.'''
        return "BSTree <"+self.__strR(self.root)+">"

    def __searchR(self, subroot, e):
        '''private recursive method to be called by search().
        it searches the subtree rooted at subroot and returns the node
        found or None if it cannot be found.''' 
        if subroot==None: return None
        if e < subroot.element:
            return self.__searchR(subroot.leftchild, e)
        elif e > subroot.element:
            return self.__searchR(subroot.rightchild, e)
        return subroot
        
    def search(self, e):
        '''Searches the tree for node containing e, Returns the Node if
        it is found or None if it is not.'''
        return self.__searchR(self.root, e)


    def __unknown(self, subroot, alist):
        if not subroot:
            return
        if subroot.isleaf:
            alist.append(subroot.element)
            return
        if subroot.hasrightchild:
            self.__unknown(subroot.rightchild, alist)
        alist.append(subroot.element)
        if subroot.hasleftchild:
            self.__unknown(subroot.leftchild, alist)
        

    def unknown(self):
        retlist=[]
        self.__unknown(self.root, retlist)
        return retlist

    def __height(self, subroot):
        pass

    #Please implement
    def height(self):
        return self.__height(self.root)



if __name__ == '__main__':
    #Put testing code here
    elements = [23, 45, 78, 12, 22, 90, 5]
    bstree = BSTree()
    for item in elements:
        bstree.add(item)
    print(bstree)
    unknown=bstree.unknown()
    print(unknown)
