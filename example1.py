def mysplit(string):
    if string.strip() == "":
        return []

    list_split = []
    word = ""

    for char in string:
        if char == " ":
            if word:
                list_split.append(word)
            word = ""
        else:
            word += char

    if word:
        list_split.append(word)

    return list_split


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
