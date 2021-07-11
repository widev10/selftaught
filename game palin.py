

#belajar algoritma palindrome( algor yang mengecek sebuah kata dibolak balik akan tetap sama )

def is_palindrome(word):
    word = word.lower()
    return word [::-1] == word

kata = input ("Please input your word :")
result = is_palindrome(kata)
print(result)