def is_palindrome(word):
    word = word.replace(" ", "").lower()
    
    if len(word) <= 1:
        return True
    

    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False
word = "kayak"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

