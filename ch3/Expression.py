from SqStack import SqStack


def is_optr(c):
# 判断c是否为运算符
    return c in ['+', '-', '*', '/', '(', ')', '#']


def precede(theta1, theta2):
# 判断运算符优先级
    if (theta1 == '(' and theta2 == ')') or (theta1 == '#' and theta2 == '#'):
        return '='
    elif theta1 == '(' or theta1 == '#' or theta2 == '(' or ((theta1 == '+' or theta1 == '-') and (theta2 == '*' or theta2 == '/')):
        return '<'
    else:
        return '>'


def operate(a, theta, b):
#计算表达式 a treta b的结果
    if theta == '+':
        return a + b
    if theta == '-':
        return a - b
    if theta == '*':
        return a * b
    if theta == '/':
        return a / b


def evaluate_expression(e):
# 求表达式e的值，e以#结尾
    opnd = SqStack()  # 初始化opnd栈
    optr = SqStack()  # 初始化optr栈
    optr.push('#')  # 将表达式起始符“#”压入optr栈
    i = 0
    while e[i] != '#' or optr.get_top() != '#':
        if not is_optr(e[i]):  # 不是运算符则进opnd栈
            opnd.push(int(e[i]))
            i += 1
        else:
            if precede(optr.get_top(), e[i]) == '<':  # 比较optr的栈顶元素和e[i]的优先级
                optr.push(e[i])  # 当前字符e[i]压入OPTR栈
                i += 1  # 下标指向下一字符
                continue
            if precede(optr.get_top(), e[i]) == '>':
                theta = optr.pop()  # 弹出optr栈顶的运算符
                b , a = opnd.pop(), opnd.pop()  # 弹出opnd栈顶的两个运算数
                opnd.push(operate(a, theta, b))  # 将运算结果压入opnd栈
                continue
            if precede(optr.get_top(), e[i]) == '=':  # optr的栈顶元素是“(”且e[i]是“)”
                optr.pop()  # 弹出optr栈顶的“(”
                i += 1  # 下标指向下一字符
                continue
    return opnd.get_top()  # opnd栈顶元素即为表达式求值结果


if __name__ == "__main__":
    print('1+2=', evaluate_expression('1+2#'))
    print('1+2/2+3*3=', evaluate_expression('1+2/2+3*3#'))
    print('1+2*5+(1+2)*3=', evaluate_expression('1+2*5+(1+2)*3#'))