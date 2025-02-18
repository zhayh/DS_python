from ch2.LinkList import LinkList


class StackNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkStack:
    def __init__(self):
        # 初始化链栈
        self.top = None  # 构造一个空栈，栈顶指针top置空

    def push(self, e):
        # 在栈顶插入元素e
        p = StackNode(data=e)  # 生成新结点，将新结点数据域置为e
        p.next = self.top  # 将新结点插入栈顶
        self.top = p  # 修改栈顶指针为p

    def pop(self):
        # 将栈顶元素弹出
        if self.top is None:
            raise Exception('栈已空')
        e = self.top.data  # 将栈顶元素赋给e
        self.top = self.top.next  # 修改栈顶指针
        return e

    def get_top(self):
        # 返回栈顶元素，不修改栈顶指针
        if self.top is not None:  # 栈非空
            return self.top.data
        else:
            raise Exception('栈已空')

    def __len__(self):
        p = self.top
        count = 0
        while p is not None:
            p = p.next
            count += 1
        return count


if __name__ == "__main__":
    s = LinkStack()
    s.push(0)
    s.push(1)
    print('栈的长度为：', len(s))

    print('此时的栈顶元素为：', s.get_top())
    s.pop()
    print('此时的栈顶元素为：', s.get_top())
