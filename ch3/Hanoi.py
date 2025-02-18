m = 0


def move(A, n, C):
    global m
    m += 1
    print("{0}, {1}, {2}, {3}".format(m, n, A, C))
    # print("第{0}步, 将编号为{1}的圆盘,从第{2}个柱子移到第{3}个柱子上".format(m, n, A, C))


def hanoi(n, A, B, C):
    # 将塔座A上的n个圆盘按规则搬到C上，B做辅助塔
    if n == 1:
        move(A, 1, C)
        # 将编号为1的圆盘从A移到C
    else:
        hanoi(n-1, A, C, B)
        # 将A上编号为1至n-1的圆盘移到B，C做辅助塔
        move(A, n, C)
        # 将编号为n的圆盘从A移到C
        hanoi(n-1, B, A, C)
        # 将B上编号为1至n-1的圆盘移到C，A做辅助塔


if __name__ == "__main__":
    n = 4
    a, b, c = 'a', 'b', 'c'
    print('初始第一个柱子上的圆盘个数：', n)
    print('将第一个柱子上的圆盘全部移动到第三个柱子上的过程为：')
    hanoi(n, a, b, c)