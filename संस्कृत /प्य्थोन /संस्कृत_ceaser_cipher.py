def sanskrit_substitution_cipher(text, mapping):
    ciphered_text = ""
    for char in text:
        if char in mapping:
            ciphered_text += mapping[char]
        else:
            ciphered_text += char
    return ciphered_text

def sanskrit_substitution_decipher(text, reverse_mapping):
    deciphered_text = ""
    for char in text:
        if char in reverse_mapping:
            deciphered_text += reverse_mapping[char]
        else:
            deciphered_text += char
    return deciphered_text

# Example mapping for substitution cipher
sanskrit_alphabet = "अआइईउऊऋॠऌॡएऐओऔअंःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह"
shift = 3
cipher_mapping = {}
reverse_mapping = {}
for i in range(len(sanskrit_alphabet)):
    cipher_mapping[sanskrit_alphabet[i]] = sanskrit_alphabet[(i + shift) % len(sanskrit_alphabet)]
    reverse_mapping[sanskrit_alphabet[(i + shift) % len(sanskrit_alphabet)]] = sanskrit_alphabet[i]

# Original Sanskrit text
sanskrit_text = "संस्कृतम्"

# Applying the substitution cipher
ciphered_text = sanskrit_substitution_cipher(sanskrit_text, cipher_mapping)

# Decrypting the ciphered text
deciphered_text = sanskrit_substitution_decipher(ciphered_text, reverse_mapping)

print("Original Sanskrit Text: " + sanskrit_text)
print("Ciphered Text: " + ciphered_text)
print("Deciphered Text: " + deciphered_text)
