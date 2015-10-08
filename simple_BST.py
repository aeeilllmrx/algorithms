

class BST():

    def __init__(self, root, parent=None):

        self.root = root
        self.left = None
        self.right = None
        self.parent = parent

    def insert(self, val):

        if val > self.root:
            if not self.right:
                self.right = BST(val, self)
            else:
                self.right.insert(val)

        else:
            if not self.left:
                self.left = BST(val, self)
            else:
                self.left.insert(val)

    def find(self, val):

        if val == self.root:
            return True
        elif val < self.root and self.left:
            return self.left.find(val)
        elif val > self.root and self.right:
            return self.right.find(val)

        return False

    def get_min(self):

        if not self.left:
            return self
        else:
            return self.left.get_min()

    def get_max(self):

        if not self.right:
            return self
        else:
            return self.right.get_max()



    def get_succ(self):

        if self.right:
            return self.right.get_min()

        # otherwise you need to keep going up until you were the left child
        else:
            cur = self
            while cur == self.parent.right:
                cur = self.parent
            if cur.parent:
                return cur.parent.right.get_min()
            else:
                return None

    def delete(self):

        # with 0 or 1 children, the case is simple
        # either make the parent connect to None, or the single child

        if not (self.left or self.right):
            if self == self.parent.left:
                self.parent.left = None
            else:
                self.parent.right = None

        elif not self.right and (self == self.parent.left):
            self.parent.left = self.left
        
        elif not self.left and (self == self.parent.right):
            self.parent.right = self.right

        else:
            s = self.get_succ()
            self.root = s.root
            s.delete()

    def BFS_print(self):

        # top to bottom
        q = [self]
        while q:
            cur = q.pop(0)
            print cur.root
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    def DFS_print(self):

        # in order
        s = [self]
        while s:
            cur = s.pop()
            print cur.root
            if cur.left:
                cur.left.DFS_print()
            if cur.right:
                cur.right.DFS_print()


b = BST(5)
b.insert(3)
b.insert(8)
b.insert(7)
b.insert(19)
b.insert(4)

minv = b.get_min()
maxv = b.get_max()
succ = b.left.get_succ()

assert b.find(2) == False
assert b.find(3) == True
assert b.find(4) == True

assert minv.root == 3
assert maxv.root == 19
assert succ.root == 4

print "\ntop to bottom:"
b.BFS_print()
print "\nin order:"
b.DFS_print()

print "\ndeleting 3, 19, 5"
b.get_min().delete()
b.get_max().delete()
b.delete()
b.BFS_print()






