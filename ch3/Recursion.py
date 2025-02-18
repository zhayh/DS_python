from ch2.LinkList import LinkList


def traverse_list(p):
    # 递归遍历链表的各个节点
    if p is None:  # 递归终止
        return
    else:
        print(p.data)  # 输出当前结点的数据域
        traverse_list(p.next)  # p指向后继结点继续递归


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def x(n):
    if n <= 3:
        return 1
    else:
        return x(n - 2) + x(n - 4) + 1


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    l = LinkList()
    l.create_list_r(data)
    p = l.head
    print('递归遍历输出链表：')
    traverse_list(p)