# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def foo(s: str) -> str:
    return s.replace('!', '')

print(foo("Hi! Hello!")) # "Hi Hello"
print(foo("")) # ""
print(foo("Oh, no!!!")) # "Oh, no"



# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove(s: str) -> str:
    if s.endswith('!'):
        return s[:-1]
    else:
        return s

print(remove("Hi!")) # "Hi"
print(remove("Hi!!!")) # "Hi!!"
print(remove("!Hi")) # "!Hi"


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove(s: str) -> str:
    words = s.split()
    new_words = []
    for word in words:
        if word.count('!') != 1:
            new_words.append(word)
    return ' '.join(new_words)

print(remove("Hi!")) # ""
print(remove("Hi! Hi!")) # ""
print(remove("Hi! Hi! Hi!")) # ""
print(remove("Hi Hi! Hi!")) # "Hi"
print(remove("Hi! !Hi Hi!")) # ""
print(remove("Hi! Hi!! Hi!")) # "Hi!!"
print(remove("Hi! !Hi! Hi!")) # "!Hi!"
