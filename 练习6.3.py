#实现判断一个数是不是素数的函数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True
# 测试函数
print(is_prime(2))  # 输出 True
print(is_prime(4))  # 输出 False
print(is_prime(17))  # 输出 True
print(is_prime(100))  # 输出 False
print(is_prime(101))  # 输出 False