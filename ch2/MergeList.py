from LinkList import LinkList
from SqList import SqList


def merge_list(la, lb):
    # 将所有在线性表lb中但不在la中的数据元素插入到la中
    m = len(la) # 求线性表la的长度
    for p in lb:  # 用p遍历lb中的数据元素
        if la.locate_elem(p.data) is None:  # la中不存在和p相同的数据元素
            m += 1  # la的长度加1
            la.list_insert(m, p.data)  # 将p.data插在la最后


def merge_list_sq(la, lb):
    lc = SqList()
    i, j, k = 1, 1, 1
    while i <= len(la) and j <= len(lb):  # la和lb均未到达表尾
        if la.get_elem(i) <= lb.get_elem(j):
            # 依次“摘取”两表中值较小的结点插入到lc的最后
            lc.list_insert(k, la.get_elem(i))
            i += 1
        else:
            lc.list_insert(k, lb.get_elem(j))
            j += 1
        k += 1
    while i <= len(la):
        # lb已到达表尾，依次将la的剩余元素插入lc的最后
        lc.list_insert(k, la.get_elem(i))
        i += 1
        k += 1
    while j <= len(lb):
        # la已到达表尾，依次将lb的剩余元素插入lc的最后
        lc.list_insert(k, lb.get_elem(j))
        j += 1
        k += 1
    return lc

def merge_list_l(la, lb):
    # 已知单链表la和lb的元素按值非递减排列
    # 归并la和lb得到新的单链表lc，lc的元素也按值非递减排列

    pa, pb = la.head.next, lb.head.next  # pa和pb的初值分别指向两个表的第一个结点
    lc = la  # la的头结点作为lc的头结点
    pc = lc.head  # pc的初值指向lc的头结点
    while pa is not None and pb is not None:
        if pa.data <= pb.data:  # “摘取”pa所指结点
            pc.next = pa  # 将pa所指结点链接到pc所指结点之后
            pc = pa  # pc指向pa
            pa = pa.next  # pa指向下一结点
        else:  # “摘取”pb所指结点
            pc.next = pb  # 将pb所指结点链接到pc所指结点之后
            pc = pb  # pc指向pb
            pb = pb.next  # pb指向下一结点
    pc.next = pa if pa is not None else pb
    return lc  # 返回合并后的链表lc


if __name__ == "__main__":
    la_data = [7, 5, 3, 11]
    lb_data = [2, 6]
    la = LinkList()
    lb = LinkList()
    la.create_list_r(la_data)
    lb.create_list_r(lb_data)
    merge_list(la, lb)
    print('合并后的线性表为：', la)

    la_data = [3, 5, 8, 11]
    lb_data = [2, 6, 8, 9, 11, 15, 20]
    la = SqList()
    lb = SqList()
    for idx, data in enumerate(la_data):
        la.list_insert(idx + 1, data)
    for idx, data in enumerate(lb_data):
        lb.list_insert(idx + 1, data)
    lc = merge_list_sq(la, lb)
    print('合并后的顺序有序表为：', lc)

    la = LinkList()
    lb = LinkList()
    la.create_list_r(la_data)
    lb.create_list_r(lb_data)
    lc = merge_list_l(la, lb)
    print('合并后的链式有序表为：', lc)
