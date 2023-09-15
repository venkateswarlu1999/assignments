# class Node:
#     def __init__(self,item):
#         self.val = item
#         self.right = None
#         self.left = None
        
# def preorder(root):
#     if root is not None:
#         print(root.val)
#         preorder(root.left)
#         preorder(root.right)
            
# def inorder(root):
#     if root is not None:
#         inorder(root.left)
#         print(root.val)
#         inorder(root.right)
# def postorder(root):
#     if root is not None:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.val)
        
        
        
# root=Node("A")
# root.left =Node("F")
# root.left.left = Node("Y")
# root.left.right = Node("X")
# root.right = Node("K")
# root.right.right = Node("T")



# preorder(root)
# inorder(root)
# postorder(root)
        
        
        
class RootNode:
    def __init__(self,item):
        self.val = item
        self.right = None
        self.left = None

def preorder(root):
    if not root:
        return("tree is empty")
    else:

        queu = []
        queu.append(root)
        node = queu.pop(0)

        while queu:
            print(node.val)

            if node.left:
                queu.append(node.left)

            if node.right:
                queu.append(node.right)


def inorder(root):
    if not root:
        return("tree is empty")
    else:

        queu = []
        queu.append(root)
        node = queu.pop(0)

        while queu:
            
           

            if node.left:
                queu.append(node.left)
            
            print(node.val)
            
            if node.right:
                queu.append(node.right)
    # if root is None:
    #     return []

    # stack = []
    # result = []
    # current = root

    # while stack or current:
    #     if current:
    #         stack.append(current)
    #         current = current.left
    #     else:
    #         node = stack.pop()
    #         result.append(node.value)
    #         current = node.right

    # return result

def postorder(root):
    if not root:
        return("tree is empty")
    else:

        queu = []
        queu.append(root)
        node = queu.pop(0)

        while queu:
            
            if node.left:
                queu.append(node.left)

            if node.right:
                queu.append(node.right)
                
            print(node.val)
             
             
    # if not root:
    #     return []

    # stack = [root]
    # result = []

    # while stack:
    #     node = stack.pop()
    #     result.append(node.value)

    #     if node.left:
    #         stack.append(node.left)

    #     if node.right:
    #         stack.append(node.right)

    # return result[::-1]

# Example usage:
# Construct a simple binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5v

root = RootNode(1)
root.left = RootNode(2)
root.right = RootNode(3)
root.right.left = RootNode(6)
root.left.left = RootNode(4)
root.left.right = RootNode(5)

preorder(root)
inorder(root)
postorder(root)