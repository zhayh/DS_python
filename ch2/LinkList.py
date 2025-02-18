class LNode:
    def __init__(self, data=None):
        self.data = data  # 结点的数据域
        self.next = None  # 结点的指针域

    def __str__(self):
        return str(self.data)


class LinkList:
    def __init__(self):
        # 生成新结点作为头结点并初始化指针域和数据区域为None，头指针head指向头节点
        self.head = LNode(None)

    def __iter__(self):
        p = self.head
        while p is not None:
            yield p
            p = p.next

    def __str__(self):
        output = ''
        for idx, item in enumerate(self): # 遍历链表，调用__iter__方法
            output += '{arrow}{data}'.format(arrow=' --> ' if idx else '', data=item.data)
        return output

    def __len__(self):
        cnt = 0
        for p in self:
            cnt += 1
        return cnt - 1

    def get_elem(self, i):
        # 在带头结点的单链表中根据序号i获取元素的值
        for idx, item in enumerate(self):  # 遍历链表
            if idx == i:  # 当下标加1等于i时，返回该数据元素
                return item
        raise Exception('位置不合法')

    def locate_elem(self, e):
        # 单链表的按值查找，查找成功返回第一个符合的元素，查找失败返回None
        for p in self:  # 遍历当前链表
            if p.data == e:
                return p  # 当p的值等于e, 返回p
        return None  # 未找到返回None

    def list_insert(self, i, e):
        # 在带头结点的单链表中第i个位置插入值为e的新结点
        for idx, p in enumerate(self):  # 遍历链表
            if idx + 1 == i:
                s = LNode(e)  # 生成新结点s并将s的数据域设置为e
                s.next = p.next  # 将结点s的指针域指向结点ai
                p.next = s  # 将结点p的指针域指向结点s
                return
        raise Exception('位置不合法')

    def list_delete(self, i):
        # 删除单链表中的第i个结点
        for idx, p in enumerate(self):  # 查找第i−1个结点，p指向该结点
            if idx + 1 == i and p.next is not None:
                p.next = p.next.next  # 改变删除结点前驱结点的指针域
                return
        raise Exception('位置不合法')

    def create_list_h(self, l_data: list):
        # 前插法，根据l_data数据列表创建链表
        for data in l_data:
            p = LNode(data)  # 生成新结点p，并将p结点的数据域赋值为data
            p.next = self.head.next  # 将新结点p插入到头结点之后
            self.head.next = p

    def create_list_r(self, l_data: list):
        # 后插法，根据l_data数据列表创建链表
        r = self.head  # 尾指针r指向头结点
        for data in l_data:
            p = LNode(data)  # 生成新结点，并初始化p的数据域为data
            r.next = p  # 将新结点p插入尾结点r之后
            r = r.next  # r指向新的尾结点p


if __name__ == "__main__":
    l = LinkList()
    l.list_insert(1, 1)
    l.list_insert(2, 2)
    l.list_insert(3, 3)
    l.list_insert(4, 4)
    print('插入元素后的线性表为：', l)
    print('值为3的元素在线性表中的位置为：', l.locate_elem(3))
    l.list_delete(3)
    print('删除顺序表中的第三个元素后：', l)
    print('删除一个元素后线性表的长度为：', len(l))

    data = [1, 2, 3, 4, 5]
    h = LinkList()
    h.create_list_h(data)
    print('前插法创建单链表：', h)
    r = LinkList()
    r.create_list_r(data)
    print('后插法创建单链表：', r)
