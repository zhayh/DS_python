max_size = 100


class SqStack:
    def __init__(self):
        # 初始化顺序栈
        self.elem = [None] * max_size  # 为顺序栈动态分配一个最大容量为max_size的数组空间
        self.top, self.base = 0, 0  # top和base都指向栈底元素在顺序栈中的位置，空栈
        self.stack_size = max_size  # stack_size置为栈的最大容量max_size

    def push(self, e):
        # 将元素压入栈
        if self.top - self.base == self.stack_size:  # 栈满
            raise Exception('栈空间已满')
        self.elem[self.top] = e  # 元素e压入栈顶,栈顶指针加1
        self.top += 1

    def pop(self):
        # 将栈顶元素弹出
        if self.top == self.base:
            raise Exception('栈已空')
        self.top -= 1  # 栈顶指针减1，并返回栈顶元素
        return self.elem[self.top]

    def get_top(self):
        # 返回栈顶元素
        if self.top != self.base:  # 栈非空
            return self.elem[self.top - 1]
        else:
            raise Exception('栈已空')

    def stack_empty(self):
        # 判断栈是否为空
        return self.top == self.base

    def __len__(self):
        # 栈的长度
        return self.top - self.base


if __name__ == "__main__":
    s = SqStack()
    s.push(0)
    s.push(1)
    print('栈的长度为：', len(s))

    print('此时的栈顶元素为：', s.get_top())
    s.pop()
    s.pop()
    print('此时栈是否为空：', s.stack_empty())