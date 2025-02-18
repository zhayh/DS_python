from LinkList import LinkList, LNode


def create_polyn(d:list):
    # 输入多项式的各项系数和指数，建立表示多项式的有序链表l
    l = LinkList()
    for data in d:  # 遍历各项系数和指数
        s = LNode(data)  # 生成新结点
        pre = l.head  # pre用于保存q的前驱，初值为头结点
        q = pre.next  # q初始化，指向首元结点
        while q is not None and q.data['expn'] < data['expn']:
            # 通过比较指数找到第一个大于输入项指数的项q
            pre = q
            q = q.next
        s.next = q
        pre.next = s   # 将输入项s插入到q和其前驱结点pre之间
    return l


def add_polyn(pa, pb):
    # 多项式加法：pa=pa + pb，利用两个多项式的结点构成“和多项式”
    p1, p2 = pa.head.next, pb.head.next  # p1和p2初值分别指向pa和pb的首元结点
    p3 = pa.head  # p3指向和多项式的当前结点
    while p1 is not None and p2 is not None:  # p1和p2均不为None
        if p1.data['expn'] == p2.data['expn']:  # 指数相等
            s = p1.data['coef'] + p2.data['coef']  # s保存两项的系数和
            if s != 0:  # 系数和不为0
                p1.data['coef'] = s  # 修改Pa当前结点的系数值为两项系数的和
                p3.next = p1  # 将修改后的Pa当前结点链在p3之后
                p3 = p1  # p3指向p1
                p1 = p1.next  # p1指向后一项
                p2 = p2.next  # p2指向后一项
            else:   # 系数和为0
                p1 = p1.next  # p1指向后一项
                p2 = p2.next  # p2指向后一项
        elif p1.data['expn'] < p2.data['expn']:  # p1当前结点的指数值小
            p3.next = p1  # 将p1链在p3之后
            p3 = p1   # p3指向p1
            p1 = p1.next  # p1指向后一项
        else:  # p2当前结点的指数值小
            p3.next = p2  # 将p2链在p3之后
            p3 = p2  # p3指向p2
            p2 = p2.next  # p2指向后一项
    p3.next = p1 if p1 is not None else p2  # 插入非空多项式的剩余段
    return pa   # 返回pa


if __name__ == "__main__":
    data_a = [{'coef': 7.0, 'expn': 0.0}, {'coef': 3.0, 'expn': 1.0}, {'coef': 9.0, 'expn': 8.0},
              {'coef': 5.0, 'expn': 17.0}]
    a = create_polyn(data_a)
    print('存储该多项式a的链表为：', a)

    data_b = [{'coef': 8.0, 'expn': 1.0}, {'coef': 22.0, 'expn': 7.0}, {'coef': -9.0, 'expn': 8.0}]
    b = create_polyn(data_b)
    print('存储该多项式b的链表为：', b)

    pc = add_polyn(a, b)
    print('多项式a与b的和为：', pc)

