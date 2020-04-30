def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input('输入文本：')
if (is_palindrome(something)):
    print("是的，这是回文")
else:
    print("不，这不是回文")
