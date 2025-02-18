class QNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkQueue:

    def __init__(self):
        # 构造一个空队列
        self.front = QNode()        # 生成新结点作为头结点，队头和队尾指针指向此结点
        self.rear = self.front

    def en_queue(self, e):
        # 插入元素e为新的队尾元素
        p = QNode(e)  # 为入队元素分配结点空间并将新结点数据域置为e，用指针p指向
        self.rear.next = p  # 将新结点插入到队尾
        self.rear = p  # 修改队尾指针

    def de_queue(self):
        # 删除队头元素，并返回
        if self.front == self.rear:  # 若队列空，则抛出异常
            raise Exception('队列已空')
        p = self.front.next  # p指向队头元素
        e = p.data  # e保存队头元素的值
        self.front.next = p.next  # 修改头结点的指针域
        if self.rear == p:  # 最后一个元素被删，队尾指针指向头结点
            self.rear = self.front
        return p

    def get_head(self):
        # 返回队头元素，不修改队头指针
        if self.front != self.rear:  # 队列非空
            return self.front.next.data  # 返回队头元素的值，队头指针不变
        else:
            raise Exception('队列已空')

    def __len__(self):
        count = 0
        p = self.front
        while p != self.rear:
            count += 1
            p = p.next
        return count


if __name__ == "__main__":
    q = LinkQueue()
    q.en_queue(1)
    q.en_queue(2)
    q.en_queue(3)
    print('队列的长度为：', len(q))
    print('队头元素为：', q.get_head())
    q.de_queue()
    print('出队后的队头元素为：', q.get_head())
    print('此时队列的长度为：', len(q))