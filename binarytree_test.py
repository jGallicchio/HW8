from binarytree import *
import unittest

class TestLabFunctions(unittest.TestCase):
    def testEvalDisp1(self):
        #tree 2
        node1 = BNode('*')

        node2 = BNode('*')
        node3 = BNode('A')
        node1.addleft(node2)
        node1.addright(node3)

        node4 = BNode('-')
        node5 = BNode('Q')

        node6 = BNode('K')
        node7 = BNode('J')

        node2.addleft(node4)
        node2.addright(node5)

        node4.addleft(node6)
        node4.addright(node7)

        self.assertEqual(node1.evaluate(), 24)
        self.assertEqual(node1.display(), '(((13-11)*12)*1)')

        #tree 1
        node1 = BNode('+')
        node2 = BNode('-')
        node3 = BNode('*')
        node1.addleft(node2)
        node1.addright(node3)

        node4 = BNode('A')
        node5 = BNode('A')

        node6 = BNode('A')
        node7 = BNode('J')

        node2.addleft(node4)
        node2.addright(node5)

        node3.addleft(node6)
        node3.addright(node7)

        self.assertEqual(node1.evaluate(), 11)
        self.assertEqual(node1.display(), '((1-1)+(1*11))')

    def testEvalDisp2(self):
        #tree 5
        node1 = BNode('/')

        node2 = BNode('8')
        node3 = BNode('-')
        node1.addleft(node2)
        node1.addright(node3)

        node4 = BNode('3')
        node5 = BNode('/')

        node6 = BNode('8')
        node7 = BNode('3')

        node3.addleft(node4)
        node3.addright(node5)

        node5.addleft(node6)
        node5.addright(node7)

        self.assertEqual(node1.evaluate(), 24)
        self.assertEqual(node1.display(), '(8/(3-(8/3)))')

        #tree3
        node1 = BNode('+')

        node2 = BNode('*')
        node3 = BNode('5')
        node1.addleft(node2)
        node1.addright(node3)

        node4 = BNode('J')
        node5 = BNode('-')

        node6 = BNode('4')
        node7 = BNode('A')

        node2.addleft(node4)
        node2.addright(node5)

        node5.addleft(node6)
        node5.addright(node7)

        self.assertEqual(node1.evaluate(), 38)
        self.assertEqual(node1.display(), '((11*(4-1))+5)')

        #tree4
        node1 = BNode('*')

        node2 = BNode('6')
        node3 = BNode('-')
        node1.addleft(node2)
        node1.addright(node3)

        node4 = BNode('+')
        node5 = BNode('2')

        node6 = BNode('3')
        node7 = BNode('9')

        node3.addleft(node4)
        node3.addright(node5)

        node4.addleft(node6)
        node4.addright(node7)

        self.assertEqual(node1.evaluate(), 60)
        self.assertEqual(node1.display(), '(6*((3+9)-2))')

    def testEvaluateFive1(self):
        ops1 = ['*','*','-']
        s1 = ['K','J','Q','A']
        self.assertEqual(evaluatefive(ops1, s1), set(['(((13-11)*12)*1)']))

        ops1 = ['-','*','-']
        s1 = ['9','4','7','5']
        self.assertEqual(evaluatefive(ops1, s1), set(['(9-((4-7)*5))']))

    def testEvaluateFive2(self):
        ops1 = ['*','+','-']
        s1 = ['6','Q','3','J']
        self.assertEqual(evaluatefive(ops1, s1), set(['(6*(12+(3-11)))']))

        ops1 = ['-','-','*']
        s1 = ['K','7','2','9']
        self.assertEqual(evaluatefive(ops1, s1), set(['(13-(7-(2*9)))']))

    def testEvaluateFive3(self):
        ops1 = ['*','-','+']
        s1 = ['9','6','2','6']
        self.assertEqual(evaluatefive(ops1, s1), set(['((9-6)*(2+6))']))

if __name__ == '__main__':
    unittest.main()
