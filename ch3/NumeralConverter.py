from SqStack import SqStack


def conversion(n):
# 对于任意一个非负十进制数，打印输出与其等值的八进制数
    s = SqStack()  # 初始化空栈s
    if n == 0:  # 如果n为0, 直接输出0
        print(0)
    else:
        while n:  # 当n非零时,循环
            s.push(n % 8)  # 把n与8求余得到的八进制数压入栈s
            n = int(n / 8)  # n更新为n与8的商
        while not s.stack_empty():  # 当栈S非空时，循环
            e = s.pop()  # 弹出栈顶元素e
            print(e, end = '')  # 输出e


if __name__ == "__main__":
    print('8的八进制为：')
    conversion(8)