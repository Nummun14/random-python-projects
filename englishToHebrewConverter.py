convert = {"/": "q", "'": "w", "ק": "e", "ר": "r", "א": "t", "ט": "y", "ו": "u", "ן": "i", "ם": "o", "פ": "p", "ש": "a", "ד": "s", "ג": "d", "כ": "f", "ע": "g", "י": "h", "ח": "j", "ל": "k", "ך": "l", "ף": ";", ",": "'", "ז": "z", "ס": "x", "ב": "c", "ה": "v", "נ": "b", "מ": "n", "צ": "m", "ת": ",", "ץ": ",", ".": "/"}


def convert_hebrew_to_english(words):
    new_words = ""
    for i in words:
        for j in convert.keys():
            if i == j:
                new_words += convert[j]
            elif i == " ":
                new_words += " "
                break
    return new_words


def convert_english_to_hebrew(words):
    new_words = ""
    for i in words:
        for j in convert.keys():
            if i == convert[j]:
                new_words += j
            elif i == " ":
                new_words += " "
                break
    return new_words


print(convert_english_to_hebrew(""))
print(convert_hebrew_to_english(""))
