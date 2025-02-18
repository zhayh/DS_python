from SqStack import SqStack


def bracket_maching(e):
# 检验表达式e中所含括号是否正确匹配，如果匹配，则返回True，否则返回False
    s = SqStack()  # 初始化空栈
    for ch in e:
        if ch == '(' or ch == '[':  # 若ch是左括号“[”或“(”，则将其压入栈
            s.push(ch)
        if ch == ')':  # 若ch是右括号“)”
            if s.get_top() == '(' and not s.stack_empty():  # 若栈非空且栈顶元素是“(”
                s.pop()  # 将栈顶元素“(”弹出
            else:
                return False  # 否则匹配失败，返回False
        if ch == ']':  # 若ch是右括号“]”
            if s.get_top() == '[' and not s.stack_empty():  # 若栈非空且栈顶元素是“[”
                s.pop()  # 将栈顶元素“[”弹出
            else:
                return False  # 否则匹配失败，返回False
    return s.stack_empty()  # 如果栈空返回True，否则返回False。


if __name__ == "__main__":
    print('()[][()]的匹配结果为：', bracket_maching('()[][()]'))
    print('[(])的匹配结果为：', bracket_maching('[(])'))

