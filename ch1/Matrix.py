class Matrix:

    def __init__(self, m):
        # 构造一个方阵
        self.matrix = m

    def __add__(self, other):
        # 求方阵self和other的和
        n = len(self.matrix)
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                m[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(m)

    def __sub__(self, other):
        # 求方阵self和other的差
        n = len(self.matrix)
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                m[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(m)

    def __mul__(self, other):
        # 求方阵self和other的矢量积
        n = len(self.matrix)
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    m[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(m)

    def __str__(self):
        # 定义方阵的输出格式
        return str(self.matrix)


if __name__ == "__main__":
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    print('a + b的结果为：', a + b)
    print('a - b的结果为：', a - b)
    print('a * b的结果为：', a * b)
