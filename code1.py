alph = ["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
'u','v','w','x','y','z']

def decrypt(text):
    text = text.lower()
    for x in range(26):
        decrypted_text = ''
        for char in text:
            if char in alph:
                c = (alph.index(char) - x) % 26
                decrypted_text += alph[c]
            else:
                decrypted_text += char
        print(decrypted_text, "\n")

inp = input("Enter text to decrypt in one line: ")
decrypt(inp)