class Node(object):
    """节点"""
    def __init__(self, data):
        self.data = data
        self.next = None

class SQList(object):
    """单链表"""
    def __init__(self):
        self.head = None
        self.count = 0

    def headInsert(self, node):
        """头插法"""
        if self.head is None:
            self.head = node
            self.count += 1
        else:
            t = self.head
            self.head = node
            self.head.next = t
            self.count += 1

    def append(self, node):
        """在尾部追加元素"""
        if self.head is None:
            self.head = node
            self.count += 1
        else:
            p = self.head
            # *p=L就是p指向L指向的第一个元素吗？
            # 下面这种写法虽然可以将数据插入到p指向的位置，但是这个数据和前面的链表已经断开了，并不能将数据插入到单链表中，
            # while p is not None:
            #     p = p.next
            # p = node
            while p.next is not None:
                p = p.next
            p.next = node
            self.count += 1

    def ListLength(self):
        """输出单链表的长度"""
        n=0
        p=self.head
        while p is not None:
            n+=1
            p=p.next
        print("链表长度为："+str(n))

    def ListEmpty(self):
        p=self.head
        if p is None:
            print("链表为空")
        else:
            print("链表不为空")

    def printspe(self):
        p=self.head
        j=0
        i=3
        while(j<i-1 and p is not None):
            p=p.next
            j+=1
        if p is None:
            print("元素不存在")
        else:
            print("第三个元素为："+str(p.data))

    def printpos(self):
        p=self.head
        i=1
        while(p is not None):
            if p.data==2:
                print("元素2的位置为："+str(i))
                break
            p=p.next
            i+=1
        if p is None:
            print("没有找到此元素")

    def insertspe(self,node):
        p=self.head
        i=3
        j=0
        while(j<i-2 and p is not None):
            p=p.next
            j+=1
        if p is None:
            print("无法插入")
        else:
            t=p.next
            p.next=node
            p=p.next
            p.next=t
            print("在第3个元素位置上插入元素5：")

    def deletespe(self):
        i=3
        j=0
        p=self.head
        while(j<i-2 and p is not None):
            j+=1
            p=p.next
        if p is None:
            print("未找到，无法删除")
        else:
            t=p.next
            p.next=t.next
            print("删除第三个元素：")
            self.count-=1


    def print(self):
        """打印链表中的所有元素"""
        p = self.head
        if p is None:
            return
        while p is not None:
            print(p.data)
            p = p.next

    def delete(self):
        print("删除链表")
        self.head=None
        self.count=0



if __name__ == '__main__':
    sqlist = SQList()
    node = Node(2)
    node1 = Node(3)
    # sqlist.print()
    sqlist.append(node)
    sqlist.append(node1)
    node2 = Node(4)
    sqlist.headInsert(node2)
    sqlist.print()
    sqlist.ListLength()
    sqlist.ListEmpty()
    sqlist.printspe()
    sqlist.printpos()
    node3=Node(5)
    sqlist.insertspe(node3)
    sqlist.print()
    sqlist.deletespe()
    sqlist.print()
    sqlist.delete()
    sqlist.print()