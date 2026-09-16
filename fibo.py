# 模块是包含 Python 定义和语句的文件。其文件名是模块名加后缀名 .py 。
# 在模块内部，通过全局变量 __name__ 可以获取模块名（即字符串）。例如，
# 用文本编辑器在当前目录下创建 fibo.py 文件，输入以下内容：

def fib(n):
    """Write Fibnacci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def fib2(n):
    """Return Febonacci series up to n"""
    result = []
    a, b = 0 ,1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    print(__name__)