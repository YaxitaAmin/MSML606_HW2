import csv
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HomeWork2:

    # Problem 1: Construct an expression tree (Binary Tree) from a postfix expression
    # input -> list of strings (e.g., [3,4,+,2,*])
    # this is parsed from p1_construct_tree.csv (check it out for clarification)

    # there are no duplicate numeric values in the input
    # support basic operators: +, -, *, /

    # output -> the root node of the expression tree. Here: [*,+,2,3,4,None,None]
    # Tree Node with * as root node, the tree should be as follows
    #         *
    #        / \
    #       +   2
    #      / \
    #     3   4

    def constructBinaryTree(self, input) -> TreeNode:
        tree1 = []
        operators = {"+", "-", "*", "/"}
        top = -1
        for value in input:
            if value not in operators:
                try:
                    float(value)
                except ValueError:
                    raise ValueError("invalid token"+ value)
                node = TreeNode(value)
                tree1.append(node)
                top+=1 #erro2 doing top-=1 realized top goes up not down
            else:
                try:
                    node_r = tree1.pop() #rightside of node
                    node_l = tree1.pop() #left node
                except IndexError:
                    raise ValueError("indexerror pop from EMPTY list")
                #error1 as noticed trying to pop elements without changing top so top-2
                top-=2
                node = TreeNode(value)
                node.left = node_l
                node.right = node_r
                tree1.append(node)
                top+=1
        if len(tree1)!=1:
            raise ValueError("too many operators")
        return tree1[top]

    # Problem 2.1: Use pre-order traversal (root, left, right) to generate prefix notation
    # return an array of elements of a prefix expression
    # expected output for the tree from problem 1 is [*,+,3,4,2]
    # you can see the examples in p2_traversals.csv

    def prefixNotationPrint(self, head: TreeNode) -> list:
        if head is None:
            return []
        else:
            # tree2 =[]
            # headN= tree2.append(head.val)
            # leftN = tree2.append(self.prefixNotationPrint(head.left))
            # rightN=tree2.append(self.prefixNotationPrint(head.right))
            
            #erro3 trying to do preorder in right,left but it should be left,right
            #error4 using apend in recursive result which gave me nested list therefor using + operator without .append()
            
            return [head.val] + self.prefixNotationPrint(head.left) + self.prefixNotationPrint(head.right)

    # Problem 2.2: Use in-order traversal (left, root, right) for infix notation with appropriate parentheses.
    # return an array of elements of an infix expression
    # expected output for the tree from problem 1 is [(,(,3,+,4,),*,2,)]
    # you can see the examples in p2_traversals.csv
    # don't forget to add parentheses to maintain correct sequence
    # even the outermost expression should be wrapped
    # treat parentheses as individual elements in the returned list (see output)

    def infixNotationPrint(self, head: TreeNode) -> list:
        if head is None: #error5 assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed" may be left or right can be empty as edge case
            return []
        if head.left is None and head.right is None:
            return [head.val]
        else:
            return ['('] + self.infixNotationPrint(head.left) + [head.val] + self.infixNotationPrint(head.right) + [')'] # left - head- right


    # Problem 2.3: Use post-order traversal (left, right, root) to generate postfix notation.
    # return an array of elements of a postfix expression
    # expected output for the tree from problem 1 is [3,4,+,2,*]
    # you can see the examples in p2_traversals.csv

    def postfixNotationPrint(self, head: TreeNode) -> list:
        if head is None:
            return []
        else:
            return self.postfixNotationPrint(head.left) + self.postfixNotationPrint(head.right)  + [head.val]# left -  right - head


class Stack:
    # Implement your stack using either an array or a list
    # (i.e., implement the functions based on the Stack ADT we covered in class)
    # You may use Python's list structure as the underlying storage.
    # While you can use .append() to add elements, please ensure the implementation strictly follows the logic we discussed in class
    # (e.g., manually managing the "top" of the stack
    
    # Use your own stack implementation to solve problem 3

    def __init__(self):
        # TODO: initialize the stack
        self.node = []
        self.top = -1
    # Problem 3: Write code to evaluate a postfix expression using stack and return the integer value
    # Use stack which you implemented above for this problem

    # input -> a postfix expression string. E.g.: "5 1 2 + 4 * + 3 -"
    # see the examples of test entries in p3_eval_postfix.csv
    # output -> integer value after evaluating the string. Here: 14

    # integers are positive and negative
    # support basic operators: +, -, *, /
    # handle division by zero appropriately

    # DO NOT USE EVAL function for evaluating the expression

    def evaluatePostfix(self, exp: str) -> int:
        # TODO: implement this using your Stack class
        operators = {"+", "-", "*", "/"}
        values = exp.split()
        if len(values) ==0: #checking empty list
            raise ValueError("empty stack")
        for value in values:

            if value not in operators:
                try:
                    float(value)
                except ValueError:
                    raise ValueError("invalid token"+ value)
                self.node.append(int(value))
                self.top +=1
            else:
                # n_right = self.node[self.top]  File "e:\MSML606\msml606_hw2_spring26\HW2.py", line 209, in <module> assert result == expected, f"Test {idx} failed: {result} != {expected}" ssertionError: Test 1 failed: 5 != 14
                #checking stack underflow
                if self.top < 1:
                    raise ValueError("too many operators")
                n_right = self.node.pop()
                self.top -=1
                
                n_left = self.node.pop()
                self.top-=1
                
                if value== '+':
                    ans = n_left + n_right
                elif value== '-':
                    ans = n_left - n_right
                elif value== '*':
                    ans = n_left * n_right
                elif value== '/':
                    if n_right == 0:raise ZeroDivisionError("devide by zero")
                    ans = n_left // n_right
                self.node.append(ans)
                self.top +=1
        # if len(values) ==0:
        #     raise ValueError("too many operators")
        #error7 try to check len value after loop which not logical move
        if self.top != 0:      # if more than 1 item left on stack top = 0 → valid top > 0 → too many operands top = -1 → empty expression / too many operators
            raise ValueError("too many operand")
        
        return self.node[self.top]
        

# Main Function. Do not edit the code below
if __name__ == "__main__":
    homework2 = HomeWork2()

    print("\nRUNNING TEST CASES FOR PROBLEM 1")
    testcases = []
    try:
        with open('p1_construct_tree.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p1_construct_tree.csv not found")

    for i, (postfix_input,) in enumerate(testcases, 1):
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)
        output = homework2.postfixNotationPrint(root)

        assert output == postfix, f"P1 Test {i} failed: tree structure incorrect"
        print(f"P1 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 2")
    testcases = []
    with open('p2_traversals.csv', 'r') as f:
        testcases = list(csv.reader(f))

    for i, row in enumerate(testcases, 1):
        postfix_input, exp_pre, exp_in, exp_post = row
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)

        assert homework2.prefixNotationPrint(root) == exp_pre.split(","), f"P2-{i} prefix failed"
        assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed"
        assert homework2.postfixNotationPrint(root) == exp_post.split(","), f"P2-{i} postfix failed"

        print(f"P2 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 3")
    testcases = []
    try:
        with open('p3_eval_postfix.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                testcases.append(row)
    except FileNotFoundError:
        print("p3_eval_postfix.csv not found")

    for idx, row in enumerate(testcases, start=1):
        expr, expected = row

        try:
            s = Stack()
            result = s.evaluatePostfix(expr)
            if expected == "DIVZERO":
                print(f"Test {idx} failed (expected division by zero)")
            else:
                expected = int(expected)
                assert result == expected, f"Test {idx} failed: {result} != {expected}"
                print(f"Test case {idx} passed")

        except ZeroDivisionError:
            assert expected == "DIVZERO", f"Test {idx} unexpected division by zero"
            print(f"Test case {idx} passed (division by zero handled)")
    print("\nRUNNING EDGE CASE TESTS FOR PROBLEM 4")

    # EC1: empty stack postfix expression
    #empty string split() gives empty listand len==0 so we raise ValueError before loop
    try:
        s = Stack()
        s.evaluatePostfix("")
        print("EC1 fail")
    except ValueError as e:
        print(f"EC1 passed  empty expression: {e}")

    # EC2 invalid token - letter instead of number
    #float("abc") raises ValueError which we catch and re-raise with message
    try:
        s = Stack()
        s.evaluatePostfix("3 abc +")
    except ValueError as e:
        print(f"EC2 passed invalid token caught: {e}")

    # EC3too few operands - operator appears before two numbers are on stack
    # self.top < 1 check catches this before popping from stack
    try:
        s = Stack()
        s.evaluatePostfix("+")
        print("EC3 FAILED")
    except ValueError as e:
        print(f"EC3 passed few operands caught: {e}")

    # EC4 many operands - extra number left on stack after evaluation
    # self.top != 0 check after loop catches leftover operands
    try:
        s = Stack()
        s.evaluatePostfix("3 4 5 +")
        print("EC4 fail")
    except ValueError as e:
        print(f"EC4 passed too many operands caught: {e}")

    # EC5division by zero
    # we check if n_right == 0 before dividing and raise ZeroDivisionError
    try:
        s = Stack()
        s.evaluatePostfix("5 0 /")
        print("EC5 fail")
    except ZeroDivisionError as e:
        print(f"EC5 passed division by zero : {e}")


# CITATION - used claude to resolve error and understand mistakes however logic and code written by yaxita
# REPORT IN README
# OUTPUT

# PS E:\MSML606\msml606_hw2_spring26> & C:/Users/YAXITA/AppData/Local/Programs/Python/Python310/python.exe e:/MSML606/msml606_hw2_spring26/HW2.py

# RUNNING TEST CASES FOR PROBLEM 1
# P1 Test 1 passed
# P1 Test 2 passed
# P1 Test 3 passed
# P1 Test 4 passed
# P1 Test 5 passed
# P1 Test 6 passed
# P1 Test 7 passed
# P1 Test 8 passed
# P1 Test 9 passed
# P1 Test 10 passed
# P1 Test 11 passed
# P1 Test 12 passed
# P1 Test 13 passed
# P1 Test 14 passed
# P1 Test 15 passed
# P1 Test 16 passed
# P1 Test 17 passed
# P1 Test 18 passed
# P1 Test 19 passed
# P1 Test 20 passed
# P1 Test 21 passed

# RUNNING TEST CASES FOR PROBLEM 2
# P2 Test 1 passed
# P2 Test 2 passed
# P2 Test 3 passed
# P2 Test 4 passed
# P2 Test 5 passed
# P2 Test 6 passed
# P2 Test 7 passed
# P2 Test 8 passed
# P2 Test 9 passed
# P2 Test 10 passed
# P2 Test 11 passed
# P2 Test 12 passed
# P2 Test 13 passed
# P2 Test 14 passed
# P2 Test 15 passed
# P2 Test 16 passed
# P2 Test 17 passed
# P2 Test 18 passed
# P2 Test 19 passed
# P2 Test 20 passed
# P2 Test 21 passed
# P2 Test 22 passed

# RUNNING TEST CASES FOR PROBLEM 3
# Test case 1 passed
# Test case 2 passed
# Test case 3 passed
# Test case 4 passed
# Test case 5 passed
# Test case 6 passed
# Test case 7 passed
# Test case 8 passed
# Test case 9 passed
# Test case 10 passed
# Test case 11 passed
# Test case 12 passed
# Test case 13 passed
# Test case 14 passed
# Test case 15 passed
# Test case 16 passed
# Test case 17 passed
# Test case 18 passed
# Test case 19 passed
# Test case 20 passed
# Test case 21 passed (division by zero handled)
# Test case 22 passed (division by zero handled)

# RUNNING EDGE CASE TESTS FOR PROBLEM 4
# EC1 passed  empty expression: empty stack
# EC2 passed invalid token caught: invalid tokenabc
# EC3 passed few operands caught: too many operators
# EC4 passed too many operands caught: too many operand
# EC5 passed division by zero : devide by zero

