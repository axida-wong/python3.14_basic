# 模块搜索路径

import sys

# 当导入一个名为 spam 的模块时，解释器首先会搜索具有该名称的内置模块。 这些模块的名称在
# sys.builtin_module_names 中列出。 如果未找到，它将在变量 sys.path 所给出的目录列
# 表中搜索名为 spam.py 的文件。 sys.path 是从这些位置初始化的:

# 被命令行直接运行的脚本所在的目录（或未指定文件时的当前目录）。

# PYTHONPATH （目录列表，与 shell 变量 PATH 的语法一样）。

# 依赖于安装的默认值（按照惯例包括一个 site-packages 目录，由 site 模块处理）。

print(sys.builtin_module_names)
print(type(sys.path))
for i in sys.path:
    print(i)