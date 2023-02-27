"""
      9
  4      20
1   6  15  170  
InOrder - [1, 4, 6, 9,15,20, 170]
PreOrder - [9, 4, 1, 6, 20, 15, 170]
PostOrder - [1, 6, 4, 15, 170, 20, 9]
"""
import json
def traverse(node):
    tree = {
        "value":node['value']
    }
    tree['left'] = None if node['left'] == None else traverse(node['left'])
    tree['right'] = None if node['right'] == None else traverse(node['right'])

    return tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value).__dict__
        else:
            newNode = Node(value).__dict__
            curNode = self.root
            while True:
                if curNode['value'] > value:
                    if curNode['left'] == None:
                        curNode['left'] = newNode
                        break
                    else:
                        curNode = curNode['left']
                        continue 
                if curNode['value'] < value:
                    if curNode['right'] == None:
                        curNode['right'] = newNode
                        break
                    else:
                        curNode = curNode['right']
                        continue 
                if curNode['value'] == value:
                    break

    def lookup(self, value):
        if self.root == None:
            return None
        else:
            curNode = self.root
            while True:
                if curNode['value'] > value:
                    if curNode['left'] == None:
                        return None
                    else:
                        curNode = curNode['left']
                        continue 
                if curNode['value'] < value:
                    if curNode['right'] == None:
                        return None
                    else:
                        curNode = curNode['right']
                        continue 
                if curNode['value'] == value:
                    return curNode

    def remove(self, value):
        if self.root == None:
            return None
        else:
            curNode = self.root
            parentNode = None
            while True:
                if curNode['value'] > value:
                    if curNode['left'] == None:
                        return None
                    else:
                        parentNode = curNode
                        curNode = curNode['left']
                        continue 
                if curNode['value'] < value:
                    if curNode['right'] == None:
                        return None
                    else:
                        parentNode = curNode
                        curNode = curNode['right']
                        continue 
                if curNode['value'] == value:
                    if curNode['right'] == None and curNode['left'] == None:
                        if parentNode['value'] > curNode['value']:
                            parentNode['left'] = None
                        else:
                            parentNode['right'] = None
                        return
                    elif curNode['right'] == None:
                        if parentNode['value'] > curNode['value']:
                            parentNode['left'] = curNode['left']
                        else:
                            parentNode['right'] = curNode['left']
                        
                        return
                    else:
                        subNode = curNode['right']
                        parentNode = curNode
                        while True:
                            if subNode['left'] == None:
                                curNode['value'] = subNode['value']
                                if subNode['right']:
                                    self.insert(subNode['right']['value'])
                                else:
                                    if parentNode['value'] == curNode['value']:
                                        parentNode['right'] = None
                                return
                            else:
                                parentNode = subNode
                                subNode = subNode['left']

    def BFS(self):
        currentNode = self.root
        arr = []
        queue = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop(0)
            arr.append(currentNode['value'])
            if currentNode['left']:
                queue.append(currentNode['left'])
            if currentNode['right']:
                queue.append(currentNode['right'])

        return arr

    def BFSR(self, queue, list):
        if len(queue) == 0:
            return list
        currentNode = queue.pop(0)
        list.append(currentNode['value'])
        if currentNode['left']:
            queue.append(currentNode['left'])
        if currentNode['right']:
            queue.append(currentNode['right'])

        return self.BFSR(queue, list)

    def DFSInOrder(self):
        return traverseInOrder(self.root, [])

    def DFSPreOrder(self):
        return traversePreOrder(self.root, [])


    def DFSPostOrder(self):
        return traversePostOrder(self.root, [])
        

    def __str__(self):
        return f"{self.root}"

def traverseInOrder(node, arr):
    if node['left']:
        traverseInOrder(node['left'], arr)
    arr.append(node['value'])
    if node['right']:
        traverseInOrder(node['right'], arr)

    return arr

def traversePreOrder(node, arr):
    arr.append(node['value'])

    if node['left']:
        traversePreOrder(node['left'], arr)
    if node['right']:
        traversePreOrder(node['right'], arr)

    return arr

def traversePostOrder(node, arr):
    if node['left']:
        traversePostOrder(node['left'], arr)

    if node['right']:
        traversePostOrder(node['right'], arr)
    arr.append(node['value'])

    return arr

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# tree.remove(170)
# print(tree.DFSPostOrder())
# print(tree.BFSR([tree.root], []))
# print(tree.BFS())
# print(traverse(tree.root))
# print(tree.lookup(4))