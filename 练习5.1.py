#生成斐波那契数列的前20个数。用Python
def fibonacci(n):
    fib_list = [1, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[:n] 
print(fibonacci(20))

 
