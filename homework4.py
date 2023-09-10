def is_palindrome(s):
    reversed_str = s[::-1]
    if s == reversed_str:
        return True
    else:
        return False
    
print(is_palindrome("лепсспел"))
print(is_palindrome("helloworld")) 