# -*- coding: UTF-8 -*-

# 20180531 处理txt 文档，每行只有一个字符串，否则错误

# 第一种方案，最后转化成了浮点数
# with open('test.txt', 'r') as f:  
#     data = f.readlines()  #txt中所有字符串读入data  
#     for line in data:  
#         odom = line.split()        #将单个数据分隔开存好  
#         numbers_float =map(float, odom)  #转化为浮点数  
#         print numbers_float  


# 我现在想转换成字符串

# with open('test.txt', 'r') as f:
#     mapping_file_lines = f.readlines()
# mobile_arr = []
# for line in mapping_file_lines:
#     if line:
#         mobile_arr.append(line.strip()
# print(mobile_arr)


# ['123                   \n', '456\n', '789\n', '123\n', '456\n', '789\n', '123\n', '456\n', '789\n', '123\n', '456\n', '789\n', '123\n', '456\n', '789\n', '123\n', '456\n', '789\n']

print('start')
a=0
while a<10e7:
    a +=1
print('end')
print(a)

# TypeError: range() integer end argument expected, got float.

# 1e10 等待的时间已经非常久了。