#写一个程序判断输入的正整数是不是回文素数。
def is_palindrome(n):
    # 将数字转换为字符串并反转
    s = str(n)
    r = s[::-1]
    # 判断反转后的字符串是否与原字符串相等
    if s == r:
        return True
    else:
        return False
def is_prime(n):
    # 判断一个数是否为素数
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
            break
        else:
            return True
            break     
def is_palindrome_prime(n):
    # 判断一个数是否为回文素数
    if is_palindrome(n) and is_prime(n):
        return True
    else:
        return False 
# 获取用户输入的正整数
num = int(input("请输入一个正整数："))
# 判断并输出结果
if is_palindrome_prime(num):
    print(f"{num} 是一个回文素数。")  
else:
    print(f"{num} 不是一个回文素数。")
