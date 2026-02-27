# MSML606_HW2 - Yaxita Amin

## Overview

This assignment implements expression trees using binary trees, tree traversal algorithms (prefix, infix, postfix), and stack-based postfix expression evaluation.

---

## Part I - Programming

### Problem 1: Construct Expression Tree

Built a binary tree from a postfix expression by using a stack. Numbers are pushed as leaf nodes, and when an operator is found, two nodes are popped and become the left and right children of the new operator node.

**Errors I made and fixed:**

- error1: Was not updating `top` after popping two nodes, fixed by doing `top -= 2`
- error2: Was doing `top -= 1` when pushing a node, but top should go UP not down, fixed to `top += 1`

### Problem 2: Tree Traversals

Implemented three traversal methods recursively:

- **Prefix** (root → left → right): return `[head.val] + left + right`
- **Infix** (left → root → right): wrap with parentheses, return `['('] + left + [head.val] + right + [')']`
- **Postfix** (left → right → root): return `left + right + [head.val]`

**Errors I made and fixed:**

- error3: Had left and right swapped in prefix traversal
- error4: Used `.append()` on recursive result which gave nested lists, fixed by using `+` operator instead
- error5: Missing leaf node base case in infix — nodes with no children should return just `[head.val]` with no parentheses

### Problem 3: Stack-based Postfix Evaluation

Evaluated postfix expressions using a manual stack (list with `top` pointer). Split expression by spaces, push numbers, pop two operands when operator found, push result back.

**Errors I made and fixed:**

- error6: Was reading `self.node[self.top]` without actually removing elements using `.pop()`, so stale values stayed in list causing wrong results
- error7: Tried to check `len(values) == 0` after the loop which is illogical — moved the empty check before the loop

---

## Problem 4: Edge Case Handling

### EC1: Empty Expression

If an empty string is passed to `evaluatePostfix`, calling `.split()` returns an empty list. I check `len(values) == 0` before the loop starts and raise a `ValueError` to prevent processing an empty input.

### EC2: Invalid Token

If a token like `"abc"` appears that is not an operator, I try `float(value)` which raises a `ValueError` for non-numeric strings. I catch this and re-raise with a descriptive message.

### EC3: Too Few Operands (Stack Underflow)

If an operator appears before enough numbers are on the stack (e.g., `"+ 3 4"`), `self.top < 1` will be True, so I raise a `ValueError` before attempting to pop.

### EC4: Too Many Operands

After the loop, if `self.top != 0` it means more than one item is left on the stack — the expression had too many numbers and not enough operators. I raise a `ValueError` in this case.

### EC5: Division by Zero

Before performing division, I check if `n_right == 0` and raise a `ZeroDivisionError` with a message to prevent a crash.

---

## AI Usage Statement

I used Claude (Anthropic) as a debugging and guidance tool to help identify mistakes in my code. All logic, code writing, and understanding is my own work. Claude helped me understand what was wrong but I wrote and fixed all code myself.

---
