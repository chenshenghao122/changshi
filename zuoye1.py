import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 从Excel文件中读取矩阵 m1
m1_df = pd.read_excel('m1.xlsx', header=None)

# 将DataFrame转换为Numpy数组
m1 = m1_df.values

# 定义区间
intervals = np.arange(0, 1.1, 0.1)

# 初始化一个数组用于存储每个区间的计数
counts = np.zeros(len(intervals) - 1)

# 统计每个区间内的元素个数
for i in range(len(intervals) - 1):
    counts[i] = np.sum((m1 >= intervals[i]) & (m1 < intervals[i+1]))

# 打印结果
for i in range(len(intervals) - 1):
    print(f'Interval [{intervals[i]}, {intervals[i+1]}) count: {counts[i]}')

# 定义区间标签
labels = [f'[{intervals[i]}, {intervals[i+1]})' for i in range(len(intervals) - 1)]

# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(labels, counts, color='skyblue')
plt.xlabel('Intervals')
plt.ylabel('Counts')
plt.title('Counts of Elements in Each Interval')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()

# 绘制饼状图
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=labels, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Counts of Elements in Each Interval')
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.show()


