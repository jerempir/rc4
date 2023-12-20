def prga(s, i, j):
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    s[i], s[j] = s[j], s[i]
    return s[(s[i] + s[j]) % 256]


def rc4(key, plaintext):
    key = key.encode('latin-1')
    plaintext = plaintext.encode('latin-1')
    s = list(range(256))
    t = [key[i % len(key)] for i in range(256)]
    j = 0
    # Инициализация s-блока
    for i in range(256):
        j = (j + s[i] + t[i]) % 256
        s[i], s[j] = s[j], s[i]

    # Генерация ключевого потока и шифрование
    i = j = 0
    ciphertext = []
    kflow = []
    for char in plaintext:
        k = prga(s, i, j)
        ciphertext.append(char ^ k)
        kflow.append(k)
    ciphertext = bytes(ciphertext)
    return ciphertext.decode('latin-1'), kflow


# Пример использования
keys = "SecretKey"
our_texts = "helloWorldAndHappyNewYear"

encrypted_text, kflowEncrypted = rc4(keys, our_texts)
print("Encrypted:", encrypted_text)

decrypted_text, kflowDecrypted = rc4(keys, encrypted_text)
print("Decrypted:", decrypted_text)
