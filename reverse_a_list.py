"""Ex 3-2 Reverse a singly-linked list (not a Python list)"""

class ListNode:
    """A Simple singly-linked list node with payload"""
    def __init__(self, payload=None):
        self.payload = payload
        self.nxt = None

def make_a_list(l): # return the head element of the list
    """Input is a Python list.  Output is a singly-linked ListNode's"""
    if l is None:
        return None
    head = ListNode(l[0])
    prev = head
    for i in range(1, len(l)):
        x = ListNode(l[i])
        prev.nxt = x
        prev = x
    return head

def reverse_a_list(li): # return the head element of the list
    """Output is a reversed singly-linked ListNode's"""
    if li is None:
        return None
    this = li
    nxt = this.nxt
    this.nxt = None # terminate the list here
    while nxt:
        nxtnxt = nxt.nxt
        nxt.nxt = this
        this = nxt
        nxt = nxtnxt
    return this

def print_a_list(ll):
    """Return the ListNode's payload in a Python list"""
    lx = []
    el = ll
    while el:
        lx.append(el.payload)
        el = el.nxt
    return lx


if __name__ == "__main__":
    test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l = make_a_list(test_list)
    p = print_a_list(l)
    print(p)
    r = reverse_a_list(l)
    p = print_a_list(r)
    print(p)
