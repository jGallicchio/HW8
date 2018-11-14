from fractions import Fraction
import itertools
import sys
ops = ['+', '-', '*', '/']
d = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6' : 6, '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}

class BNode:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

    def addleft(self, leftnode):
        self.left = leftnode

    def addright(self, rightnode):
        self.right = rightnode

    def evaluate(self):
        ## Add your code here
        if self.element == ops[3] and self.right.element == 0:
            return 0
        else:
            if not self.left and not self.right:
                return d[self.element]
            elif self.element == ops[0]:
                return self.left.evaluate() + self.right.evaluate()
            elif self.element == ops[1]:
                return self.left.evaluate() - self.right.evaluate()
            elif self.element == ops[2]:
                return self.left.evaluate() * self.right.evaluate()
            elif self.element == ops[3]:
                return self.left.evaluate() / self.right.evaluate()

    def display(self):
        ## Add your code here
        if not self.left and not self.right:
            return str(d[self.element])
        elif self.element in ops:
            return '(' + self.left.display() + self.element + self.right.display() + ')'


def evaluatefive(ops, cards):

    s = set()
    # Tree #1
    node1 = BNode(ops[0])
    node2 = BNode(ops[1])
    node3 = BNode(ops[2])
    node1.addleft(node2)
    node1.addright(node3)

    node4 = BNode(cards[0])
    node5 = BNode(cards[1])

    node6 = BNode(cards[2])
    node7 = BNode(cards[3])

    node2.addleft(node4)
    node2.addright(node5)

    node3.addleft(node6)
    node3.addright(node7)

    if node1.evaluate() == 24:
        s.add(node1.display())

    # Tree #2
    ## Add your code here
    node12 = BNode(ops[0])
    node22 = BNode(ops[1])
    node32 = BNode(ops[2])

    node42 = BNode(cards[0])
    node52 = BNode(cards[1])

    node62 = BNode(cards[2])
    node72 = BNode(cards[3])

    node12.addleft(node22)
    node12.addright(node72)

    node22.addleft(node32)
    node22.addright(node62)

    node32.addleft(node42)
    node32.addright(node52)

    if node12.evaluate() == 24:
        s.add(node12.display())
    #tree #3
    ## Add your code here
    node13 = BNode(ops[0])
    node23 = BNode(ops[1])
    node33 = BNode(ops[2])

    node43 = BNode(cards[0])
    node53 = BNode(cards[1])

    node63 = BNode(cards[2])
    node73 = BNode(cards[3])

    node13.addleft(node23)
    node13.addright(node73)

    node23.addleft(node43)
    node23.addright(node33)

    node33.addleft(node53)
    node33.addright(node63)

    if node13.evaluate() == 24:
        s.add(node13.display())
    #tree #4
    ## Add your code here
    node14 = BNode(ops[0])
    node24 = BNode(ops[1])
    node34 = BNode(ops[2])

    node44 = BNode(cards[0])
    node54 = BNode(cards[1])

    node64 = BNode(cards[2])
    node74 = BNode(cards[3])

    node14.addleft(node44)
    node14.addright(node24)

    node24.addleft(node34)
    node24.addright(node74)

    node34.addleft(node54)
    node34.addright(node64)

    if node14.evaluate() == 24:
        s.add(node14.display())
    #tree #5
    ## Add your code here
    node15 = BNode(ops[0])
    node25 = BNode(ops[1])
    node35 = BNode(ops[2])

    node45 = BNode(cards[0])
    node55 = BNode(cards[1])

    node65 = BNode(cards[2])
    node75 = BNode(cards[3])

    node15.addleft(node45)
    node15.addright(node25)

    node25.addleft(node55)
    node25.addright(node35)

    node35.addleft(node65)
    node35.addright(node75)

    if node15.evaluate() == 24:
        s.add(node15.display())
    return s

s = list(input())
if len(s) != 4:
    sys.exit()
for i in range(len(s)):
    if s[i] not in d.keys():
        sys.exit()
results = set()
s1 = [0, 1, 2, 3]
for L in list(itertools.permutations([0, 1, 2, 3], 4)):
    for i in range(4):
        s1[i] = s[L[i]]

    ops1 = [ops[0], ops[0], ops[0]]
    for i in range(len(ops)):
        for j in range(len(ops)):
            for k in range(len(ops)):
                ops1[0] = ops[i]
                ops1[1] = ops[j]
                ops1[2] = ops[k]
                results = results | evaluatefive(ops1, s1)
for result in results:
    print(result)
print(str(len(results)) + " solutions.")
