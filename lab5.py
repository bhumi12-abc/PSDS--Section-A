# Infix to Postfix Conversion using Stack

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for ch in expression:
        # If operand
        if ch.isalnum():
            postfix += ch

        # If opening bracket
        elif ch == '(':
            stack.append(ch)

        # If closing bracket
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        # If operator
        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(ch)):
                postfix += stack.pop()

            stack.append(ch)

    # Pop remaining operators
    while stack:
        postfix += stack.pop()

    return postfix


# Main program
expression = input("Enter Infix Expression: ")

result = infix_to_postfix(expression)

print("Postfix Expression:", result)
# Part 2-Postfix Expression Evaluation using Stack

def evaluate_postfix(expression):
    stack = []

    for ch in expression:
        # If operand
        if ch.isdigit():
            stack.append(int(ch))

        # If operator
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                result = a + b
            elif ch == '-':
                result = a - b
            elif ch == '*':
                result = a * b
            elif ch == '/':
                result = a / b
            elif ch == '^':
                result = a ** b

            stack.append(result)

    return stack.pop()


# Main program
expression = input("Enter Postfix Expression: ")

result = evaluate_postfix(expression)

print("Result:", result)
# Part3-Binary Search Tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


# Insert a node
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)

    elif key > root.key:
        root.right = insert(root.right, key)

    return root


# Find minimum value node
def min_value_node(root):
    current = root

    while current.left is not None:
        current = current.left

    return current


# Delete a node
def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)

    elif key > root.key:
        root.right = delete(root.right, key)

    else:
        # Node with no left child
        if root.left is None:
            return root.right

        # Node with no right child
        elif root.right is None:
            return root.left

        # Node with two children
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    return root


# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Preorder Traversal
def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")


# Main Program
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)

# Delete a node
print("\n\nDeleting 30...")
root = delete(root, 30)

print("Inorder after deletion:")
inorder(root)