node = int(input())

tree = dict()

for i in range(node):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1]) 
    
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')

    
preorder('A')
print()

inorder('A')
print()

postorder('A')
print()

# 챗 지피티가 단축해준 코드

# def create_tree(node_count):
#     tree = {}
#     for _ in range(node_count):
#         root, left, right = input().split()
#         tree[root] = (left, right)
#     return tree

# def traverse(tree, node, order):
#     if node == '.':
#         return
#     left, right = tree.get(node, ('.', '.'))
#     if order == 'pre':
#         print(node, end='')
#     traverse(tree, left, order)
#     if order == 'in':
#         print(node, end='')
#     traverse(tree, right, order)
#     if order == 'post':
#         print(node, end='')

# def main():
#     node_count = int(input())
#     tree = create_tree(node_count)
    
#     for order in ['pre', 'in', 'post']:
#         traverse(tree, 'A', order)
#         print()

# if __name__ == "__main__":
#     main()
