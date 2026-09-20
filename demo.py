import sys
print(sys.argv)
print()
print()
# argparse基本结构

# 推荐 运行命令
# python demo.py testfile -o workfile -n 50 --epoch 600 --config 
# con a.txt b.txt --verbose --store_false --layer conv1 --layer 
# conv2 --mode test --inputnum 666

import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument(...)
# args = parser.parse_args()

# ArgumentParser() 创建解析器
# add_argument() 定义参数
# parse_args() 解析参数

# ArgumentParser() 定义

# argparse.ArgumentParser(
#     prog=None,
#     description=None
# )

# 创建一个解释器
parser = argparse.ArgumentParser(
    prog="demo",
    description="argparse 用法示例"
)

# 生成 usage: mytool [-h]

# add_argument() 定义

# parser.add_argument(
#     name,
#     action,
#     nargs,
#     type,
#     default,
#     required,
#     choices,
#     help
# )

# 位置参数

parser.add_argument("filename")
# 不需要 --
# 默认必须存在
# 按顺序匹配
# filename = parser.parse_args()

# 可选参数, 就是可选的开关这个option 没有参数
# parser.add_argument("--output")
# 短参数
parser.add_argument("-o", "--output")

# type 类型转换，默认都是字符串

parser.add_argument("-n", "--num", type=int)

# default默认值
parser.add_argument("--epoch", type=int, default=100)

# required 必选参数
parser.add_argument("--config", required=True)

# nargs 多个值
parser.add_argument("files", nargs="+")

# action 控制行为
# store 默认
# store_true
# 就是有这个参数的时候存储 True, 否则 False
parser.add_argument("--verbose", action="store_true")
# store_false 反过来
parser.add_argument("--store_false", action="store_false")
# append 重复参数
parser.add_argument("--layer", action="append")

# choise 限制输入
parser.add_argument("--mode", choices=["train", "test"])
# --mode train 允许， --mode abc 不允许,会报错

# help 显示帮助信息
parser.add_argument("--inputnum", type=int, help="input number")

# dest 修改变量名
# --batch-size 会变 args.batch_size
# 自动从 '-' 变 '_'
# 也可以：
# parser.add_argument(
#     "--output",
#     dest="out"
# )
# 结果：
# args.out

# parse_args()
args = parser.parse_args() # 解析
# 返回 Namespace(...)

print(args)
print(args.epoch)


