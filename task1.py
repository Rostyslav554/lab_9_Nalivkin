def caesar_cipher_advanced():
    text = input("Введіть текст для шифрування: ")

    while True:
        try:
            shift = int(input("Введіть значення зсуву (1-25): "))
            if 1 <= shift <= 25:
                break
            else:
                print("Зсув має бути між 1 та 25. Спробуй знову.")
        except ValueError:
            print("Невірне введення. Будь ласка, введіть допустиме ціле число від 1 до 25.")

    cipher = ''

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            code = (ord(char) - base + shift) % 26 + base
            cipher += chr(code)
        else:
            cipher += char

    print("Зашифрований текст:", cipher)

caesar_cipher_advanced()
