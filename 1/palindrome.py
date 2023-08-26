def palindrome(str):
    return str == str[::-1]

print(palindrome('кот'))
print(palindrome('тот'))
