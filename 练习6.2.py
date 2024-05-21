def is_palindrome(number):
    # 将数字转换为字符串
    str_num = str(number)
    # 检查字符串是否等于其反转后的字符串
    return str_num == str_num[::-1]
# 测试示例
print(is_palindrome(121))  # 输出: True
print(is_palindrome(-121)) # 输出: False
print(is_palindrome(10))   # 输出: False
