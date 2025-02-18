class LNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prior = None

    def __str__(self):
        return str(self.data)


class LinkList:
    def __init__(self):
        self.head = LNode(None)

    def __iter__(self):
        p = self.head
        while p is not None:
            yield p
            p = p.next

    def list_insert_dul(self, i, e):
        # 在第i个位置插入节点e
        for idx, p in enumerate(self):
            if idx == i:
                s = LNode(e)  # 生成新结点s,并将数据域置为e
                s.prior = p  # 将结点s插入双向链表中，此步对应图2.20①
                s.next = p.next  # 对应图2.20②
                p.next = s  # 对应图2.20③
                if s.next is not None:
                    s.next.prior = s  # 对应图2.20④
                return
        raise Exception('位置不合法')

    def list_delete_dul(self, i):
        # 删除双向链表中的第i个元素
        for idx, p in enumerate(self):
            if idx == i:
                p.prior.next = p.next  # 修改被删结点的前驱结点的后继指针，对应图2.21①
                if p.next is not None:
                    p.next.prior = p.prior  # 修改被删结点的后继结点的前驱指针，对应图2.21②
                return
        raise Exception('位置不合法')

    def __str__(self):
        output = ''
        for idx, item in enumerate(self):
            output += '{arrow}{data}'.format(arrow=' <--> ' if idx else '', data=item.data)
        return output


if __name__ == "__main__":
    l = LinkList()
    l.list_insert_dul(0, 1)
    l.list_insert_dul(1, 2)
    print('插入后的双向链表为：', l)
    l.list_delete_dul(1)
    print('删除第一个元素的双向链表为：', l)
