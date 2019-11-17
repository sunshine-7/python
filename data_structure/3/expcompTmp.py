
from stack import Node
from stack import Stack

class ExpComp(object):
    """表达式求值"""

    def __init__(self):
        self.rpri = {"=":0, "(":6, "+":2, "-":2,
                     "*":4, "/":4, ")":1}
        self.lpri = {"=":0, "(":1, "+":3, "-":3,
                     "*":5, "/":5, ")":6}

    def isOP(self, char):
        """"""
        if char=="(" or char==")" or char=="+" or char=="-"\
            or char =="*" or char=="/":
            return True
        else:
            return False

    def precede(self, op1, op2):
        """比较两个运算符的优先级"""
        if self.lpri[op1] == self.rpri[op2]:
            return 0
        elif self.lpri[op1] > self.rpri[op2]:
            return -1
        else:
            return 1

    def cal(self,n1,n2,op):
        if op=="+":
            return n2+n1
        elif op=="-":
            return n2-n1
        elif op=="*":
            return n2*n1
        else:
            if n1==0:
                return "除数为0，错误"
            else:
                return n2/n1

    def trans(self, exp):
        """把算术表达式做成后缀式的"""
        postexp = []
        op = Stack()
        op.push(Node("="))
        # pass是跳过的意思，可以用来写大概框架
        # ++++++++++
        # 如果按下面的写，会有错
        # 在for循环中的while让j+=1，并不能改变while外面j的值
        # for j in range(len(exp)):
        j=0
        # 遍历表达式
        while(j<len(exp)):
            # 前面要加上self
            # 如果是运算数，就直接将其放在postexp中，继续向下遍历，直到不是运算数，在postexp后面加上#
            if(self.isOP(exp[j]) is False):
                # 在while循环里面加上j<len(exp)，因为当循环到字符串的最后一个字符时，再向下遍历，已经超出字符串，
                # 下标越界，再进行exp[j].isdigit()时，则会出现IndexError: string index out of range
                while(j<len(exp) and exp[j].isdigit()):
                    postexp.append(exp[j])
                    j+=1
                postexp.append("#")
            # 如果是运算符，就将该运算符和op栈顶的运算符进行优先级比较
            else:
                # 这里是op.top.data(str类型)，不是op.top(node类型)
                judge=self.precede(op.top.data,exp[j])
                # 如果op栈顶运算符的优先级高，将栈顶运算符出栈并将其存入postexp中
                if judge==-1:
                    postexp.append(op.pop())
                # 如果op栈顶运算符和该运算符的优先级一样，栈顶运算符出栈
                if judge==0:
                    op.pop()
                    j+=1
                # 如果op栈顶运算符的优先级低，将该运算符入op栈
                if judge==1:
                     op.push(Node(exp[j]))
                     j+= 1
        # exp扫描完，op栈还有除了 “=”以外的运算符，将其所有存入postexp
        while(op.top.data!="="):
            postexp.append(op.pop())
        # +++++++++++
        return "".join(postexp)

    def computVal(self, postexp):
        """计算后缀式的值"""
        vstack = Stack()
        n = []
        d=0
        for char in postexp:
            isop = self.isOP(char)
            # ++++++++++++
            # 运算数
            if not isop:
                if(char!="#"):
                    d=10*d+int(char)
                else:
                    vstack.push(Node(d))
                    d=0
            # 运算符
            else:
                num1=vstack.pop()
                num2=vstack.pop()
                vstack.push(Node(self.cal(num1,num2,char)))
            # ++++++++++++
        return vstack.top.data

if __name__ == '__main__':
    expComp = ExpComp()
    exp = "10*((11-10+1)*2)+(100+1)/(3*2)+(10-9)*10/5"
    # 10#11#10#-1#+2#**100#1#+3#2#*/+10#9#-10#*5#/+
    # exp = "(56-20)/(4+2)"
    # exp = "*(++)+"
    postexp = expComp.trans(exp)
    print(postexp)
    # postexp="10#11#10#-1#+2#**100#1#+3#2#*/+10#9#-10#*5#/+"
    result = expComp.computVal(postexp)
    print(result)

# by hgg

# from stack import Node
# from stack import Stack
#
# class ExpComp(object):
#     """表达式求值"""
#
#     def __init__(self):
#         self.rpri = {"=":0, "(":6, "+":2, "-":2,
#                      "*":4, "/":4, ")":1}
#         self.lpri = {"=":0, "(":1, "+":3, "-":3,
#                      "*":5, "/":5, ")":6}
#
#     def isOP(self, char):
#         """"""
#         if char=="(" or char==")" or char=="+" or char=="-"\
#             or char =="*" or char=="/":
#             return True
#         else:
#             return False
#
#     def precede(self, op1, op2):
#         """比较两个运算符的优先级"""
#         if self.lpri[op1] == self.rpri[op2]:
#             return 0
#         elif self.lpri[op1] > self.rpri[op2]:
#             return -1
#         else:
#             return 1
#
#     def trans(self, exp):
#         """把算术表达式做成后缀式的"""
#         postexp = []
#         op = Stack()
#         op.push(Node("="))
#         flag = False
#         for char in exp:
#             isop = self.isOP(char)
#             if not isop:
#                 flag = True
#                 if char.isdigit():
#                     postexp.append(char)
#                 else:
#                     raise ValueError("只能计算数字")
#             else:
#                 if flag:    #"10*(11-10)+100"
#                     postexp.append("#")
#                     flag = False
#                 pre = self.precede(op.top.data, char)
#                 if pre == -1:
#                     while True:
#                         tnode = op.pop()
#                         postexp.append(tnode.data)
#                         pre = self.precede(op.top.data, char)
#                         if pre == 0:
#                             op.pop()
#                             break
#                         elif pre == 1:
#                             tinode = Node(char)
#                             op.push(tinode)
#                             break
#                 elif pre == 1:
#                     tinode = Node(char)
#                     op.push(tinode)
#                 elif pre == 0:
#                     op.pop()
#
#         if char.isdigit():    #urgly
#             postexp.append("#")
#
#         for i in range(op.num-1):
#             tnode = op.pop()
#             if tnode.data != "=":
#                 pre = self.precede(op.top.data, tnode.data)
#                 if pre == 0:
#                     op.pop()
#                 else:
#                     postexp.append(tnode.data)
#         return "".join(postexp)
#
#     def computVal(self, postexp):
#         """计算后缀式的值"""
#         vstack = Stack()
#         n = []
#         for char in postexp:
#             isop = self.isOP(char)
#             if not isop:
#                 if char != "#":
#                     n.append(char)
#                 else:
#                     num = "".join(n)
#                     vstack.push(Node(num))
#                     n = []
#             else:
#                 a = vstack.pop()
#                 b = vstack.pop()
#                 texp = "".join([b.data, char, a.data])
#                 result = str(eval(texp))
#                 vstack.push(Node(result))
#         return vstack.top.data
#
# if __name__ == '__main__':
#     expComp = ExpComp()
#     exp = "10*((11-10+1)*2)+(100+1)/(3*2)+(10-9)*10/5"
#     # exp = "(56-20)/(4+2)"
#     # exp = "*(++)+"
#     postexp = expComp.trans(exp)
#     print(postexp)
#     result = expComp.computVal(postexp)
#     print(result)
#
