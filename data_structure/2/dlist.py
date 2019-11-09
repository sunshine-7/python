# 定义函数的头字母用小写
class Node(object):
    """节点"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prior=None

class SQList(object):
    """双链表"""
    def __init__(self):
        self.head=None
        self.count = 0

    def headInsert(self, node):
        """头插法"""
        if self.head is None:
            self.head = node
            self.count += 1
        else:
            node.next=self.head
            self.head=node
            node.next.prior=node
            self.count += 1

    def append(self, node):
        """在尾部追加元素"""
        if self.head is None:
            self.head = node
            self.count += 1
        else:
            p = self.head
            # 下面这种写法虽然可以将数据插入到p指向的位置，但是这个数据和前面的链表已经断开了，并不能将数据插入到单链表中，
            # while p is not None:
            #     p = p.next
            # p = node
            while p.next is not None:
                p = p.next
            p.next = node
            node.prior=p
            self.count += 1

    def listLength(self):
        """输出单链表的长度"""
        # n=0
        # p=self.head
        # while p is not None:
        #     n+=1
        #     p=p.next
        # print("链表长度为："+str(n))
        # 最好有返回值，一般只需知道返回值，不用打印，
        # 直接用 return self.count
        return self.count

    def listEmpty(self):
        """判断链表是否为空"""
        # # 判断头结点是否有数据
        p=self.head
        # print("""========""")
        # print(p.data)
        if p is None:
            return True
        else:
            return False

    def printSpe(self):
        """输出某个特定位置的元素"""
        p=self.head
        j=0
        i=int(input("要查询哪个位置的元素？"))
        while(i<1):
            i = int(input("位置从1开始，请重新输入：\n"))
        while(j<i-1 and p is not None):
            p=p.next
            j+=1
        if p is None:
            print("元素不存在")
        else:
            print("第%d个元素为：" %i +str(p.data))

    def printPos(self):
        """输出某个特定元素的位置"""
        p=self.head
        i=1
        num=int(input("要查询哪个元素的位置？"))
        while(p is not None):
            if p.data==num:
                print("元素%d的位置为：" %num +str(i))
                break
            p=p.next
            i+=1
        if p is None:
            print("没有找到此元素")

    def insertSpe(self,node):
        """在某个特定的位置插入某个元素"""
        p=self.head
        print(p.data)
        i=int(input("要在哪个位置插入元素？\n"))
        while (i < 1):
            i = int(input("位置从1开始，请重新输入：\n"))
        j=0
        if i==1:
            node.next=self.head
            # 让新插入的结点成为新的头结点
            self.head=node
            node.next.prior=node
            self.count+=1
        else:
            while(j<i-2 and p is not None):
                p=p.next
                j+=1
            if p is None:
                print("无法插入")
            else:
                if j==self.count-1:
                    p.next=node
                    node.prior=p
                else:
                    node.next = p.next
                    p.next = node
                    node.next.prior = node
                    node.prior = p
                self.count+=1
        #注意，这里要这么写 %(i,int(node.data))
        print("在第%d个元素位置上插入元素%d：" %(i,int(node.data)))


    def deleteSpe(self):
        """删除某个特定位置的元素"""
        i=int(input("要删除哪个位置的元素？\n"))
        while (i < 1):
            i = int(input("位置从1开始，请重新输入：\n"))
        j=0
        p=self.head
        while p is None:
            return False
        if i==1:
            self.head=p.next
            if self.count != 1:
                p.next.prior=None
                p.next=None
        else:
            # 当跳出while循环时，p指向的是要删除的结点的前一个结点
            while(j<i-2 and p.next is not None):
                j+=1
                p=p.next
            if p.next is None:
                print("未找到，无法删除")
            else:
                t=p.next
                p.next=t.next
                t.prior=None
                if i!=self.count:
                    t.next.prior=p
                    t.next=None
        print("删除第%d个元素：" %i)
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
        """释放单链表"""
        print("释放双链表")
        self.head=None
        self.count=0


if __name__ == '__main__':
    sqlist = SQList()
    n=int(input("请输入要插入的数据：\n"))
    node = Node(n)
    n1 = int(input("请输入要插入的数据：\n"))
    node1 = Node(n1)
    sqlist.headInsert(node)
    sqlist.append(node1)
    n2 = int(input("请输入要插入的数据：\n"))
    node2 = Node(n2)
    sqlist.headInsert(node2)
    sqlist.print()
    print("链表长度："+str(sqlist.listLength()))
    if sqlist.listEmpty()==True:
        print("链表为空")
    else:
        print("链表不为空")
    sqlist.printSpe()
    sqlist.printPos()
    n3 = int(input("请输入要插入的数据：\n"))
    node3=Node(n3)
    sqlist.insertSpe(node3)
    sqlist.print()
    sqlist.deleteSpe()
    sqlist.print()
    sqlist.delete()
    sqlist.print()

