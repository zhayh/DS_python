
max_size = 100

class SqQueue:
    def __init__(self):
        # 初始化一个空队列
        self.elem = [None] * max_size      # 为队列分配一个最大容量为max_size的数组空间
        self.front, self.rear = 0, 0       # 头指针和尾指针置为零，队列为空
        self.max_size = max_size

    def __len__(self):
        # 返回队列的元素个数，即队列的长度
        return (self.rear - self.front + self.max_size) % self.max_size

    def en_queue(self, e):
        # 把元素e加入队尾
        if (self.rear + 1) % self.max_size == self.front:
            # 尾指针在循环意义上加1后等于头指针，表明队满
            raise Exception('队列已满')
        self.elem[self.rear] = e  # 新元素插入队尾
        self.rear = (self.rear + 1) % self.max_size  # 队尾指针加1

    def de_queue(self):
        # 删除队头元素并将其返回
        if self.front == self.rear:  # 队空
            raise Exception('队列已空')
        e = self.elem[self.front]  # 保存队头元素
        self.front = (self.front + 1) % self.max_size  # 队头指针加1
        return e

    def get_head(self):
        # 返回队头元素，不修改队头指针
        if self.front != self.rear:  # 队列非空
            return self.elem[self.front]  # 返回队头元素的值，队头指针不变
        else:
            raise Exception('队列已空')


if __name__ == "__main__":
    q = SqQueue()
    q.en_queue(1)
    q.en_queue(2)
    q.en_queue(3)
    print('队列的长度为：', len(q))
    print('队头元素为：', q.get_head())
    q.de_queue()
    print('出队后的队头元素为：', q.get_head())
    print('此时队列的长度为：', len(q))