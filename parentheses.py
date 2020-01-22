"""Are the parentheses in the string balanced?  And if not,
   what is the position of the first offending parenthesis?
"""

def paren_balanced(string):
    """check for balanced () in a string"""
    pstack = []
    for i, c in enumerate(string):
        if c == '(' or c == '[' or c == '{':
            pstack.append([i, c])
        if c == ')' or c == ']' or c == '}':
            if not pstack:
                # too many close paren
                return False
            else:
                pstack.pop()
    if pstack:
        # we saw the last close paren and there are still open paren on the stack
        return False
    return True
    ...

if __name__ == "__main__":
    s = '({}((a[({()))}c))]'
    balanced = paren_balanced(s)

    if balanced:
        print("The parentheses are balanced.")
    else:
        print(f"The parentheses are not balanced")

