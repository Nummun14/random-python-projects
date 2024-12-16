def decrypt(encrypted_text, n):
    odd_chars = ""
    even_chars = ""
    for i in range(n):
        for char in encrypted_text:
            print(char)
            if encrypted_text.index(char) % 2 != 0:
                odd_chars = odd_chars + char
            else:
                even_chars = even_chars + char
        encrypted_text = odd_chars + even_chars
    return encrypted_text


def encrypt(text, n):
    pass


code = "012345"
print(encrypt(code, 2))
