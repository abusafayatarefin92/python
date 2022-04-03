def translator(phrase):
    translation = ""

    for item in phrase:
        if item.lower() in "aeiou":
            if item.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += item

    return translation


print(translator(input("Insert phrases: ")))
