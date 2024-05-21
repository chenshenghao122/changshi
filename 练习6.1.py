#实现计算求最大公约数和最小公倍数的函数。
def gcd(a, b):
    while b:
        a, b = b, a % b
        return a
def lcm(a, b):
    return a * b // gcd(a, b)
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))
print("最大公约数：", gcd(num1, num2))
print("最小公倍数：", lcm(num1, num2))
