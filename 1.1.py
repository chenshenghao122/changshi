import pandas as pd
import numpy as np
# 读取Excel文件中的数据
file1 = 'm1.xlsx'
file2 = 'm2.xlsx'
# 假设数据在第一个工作表中，读取为DataFrame
df1 = pd.read_excel(file1, sheet_name=0)
df2 = pd.read_excel(file2, sheet_name=0)
# 将DataFrame转换为Numpy数组
matrix1 = df1.to_numpy()
matrix2 = df2.to_numpy()
# 获取并打印数组的尺寸
print("Matrix 1 dimensions:", matrix1.shape)
print("Matrix 2 dimensions:", matrix2.shape)

# 生成区间为[0, 1)的随机数
# 注意：假设需要对矩阵中的值重新生成在区间[0, 1)内的随机数
matrix1 = np.random.rand(*matrix1.shape)
matrix2 = np.random.rand(*matrix2.shape)

# 打印矩阵值
print("Matrix 1 values:\n", matrix1)
print("Matrix 2 values:\n", matrix2)
