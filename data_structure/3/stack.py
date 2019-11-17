class Node(object):
    """节点"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Stack(object):
    """stack"""
    def __init__(self):
        self.top = None
        self.num = 0

    def push(self, node):
        """压 stack"""
        if self.top is None:
            self.top = node
            self.num += 1
        else:
            # ++++++++
            node.next=self.top
            self.top=node
            self.num+=1
            # ++++++++



    def pop(self):
        """出stack"""
        if self.top is None:
            raise ValueError("stack中没有元素")
        else:
            # ++++++++
            e=self.top.data
            p=self.top
            self.top=p.next
            p.next=None
            self.num-=1
            return e
            # ++++++++

if __name__ == '__main__':
    stack = Stack()
    for i in range(100):
        tnode = Node(i)
        stack.push(tnode)
    for i in range(100):
        tnode = stack.pop()
        print(tnode)

# #by hgg


# class Node(object):
#     """节点"""
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __str__(self):
#         return str(self.data)
#
#
# class Stack(object):
#     """stack"""
#     def __init__(self):
#         self.top = None
#         self.num = 0
#
#     def push(self, node):
#         """压 stack"""
#         if self.top is None:
#             self.top = node
#             self.num += 1
#         else:
#             t = self.top
#             self.top = node
#             self.top.next = t
#             self.num += 1
#
#     def pop(self):
#         """出stack"""
#         if self.top is None:
#             raise ValueError("stack中没有元素")
#         else:
#             re = self.top
#             self.top = self.top.next
#             re.next = None
#             self.num -= 1
#             return re
#
# if __name__ == '__main__':
#     stack = Stack()
#     for i in range(100):
#         tnode = Node(i)
#         stack.push(tnode)
#     for i in range(1000):
#         tnode = stack.pop()
#         print(tnode)
