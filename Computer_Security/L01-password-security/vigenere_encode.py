import sys, re, nltk

file_name = sys.argv[1]
f = open(file_name, 'r')
message = f.read()
message = message.lower()

key = sys.argv[2]
key = key.lower().strip()

new_message = ""
for i, c in enumerate(message):
    num = ord(c)
    num += (ord(key[i % len(key)]) - 97)
    if num > 122 and num <= 122+26: num -= 26
    if num >= 97 and num <= 122: 
        new_c = chr(num)
        new_message += new_c
    else:
        new_message += c

print(f"Successfully encrypt the message with the key \"{key}\":\n\n")
print(new_message)