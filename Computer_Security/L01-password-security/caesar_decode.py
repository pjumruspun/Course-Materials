import sys, nltk

# Threshold acc which program consider as a succesful decipher
accuracy_threshold = 0.75

# Delimeters to be filtered out to check dictionary
delimeters = ['.', ',', ';', '-', '?', '!']

# Download dictionary
nltk.download('words')
english_vocab = set(w.lower() for w in nltk.corpus.words.words())

# File Management
file_name = sys.argv[1]
f = open(file_name, 'r')
message = f.read()
message = message.lower()
f.close()

max_acc = -1
correct_shift = -1
deciphered_message = ""

for i in range(26):
    # Try decipher with shift = i
    new_message = ""
    for c in message:
        num = ord(c)
        if num >= 97 and num <= 122: 
            num -= i
            if num < 97: num += 26
            new_c = chr(num)
            new_message += new_c
        else:
            new_message += c

    # Filter out delimeters
    for d in delimeters:
        new_message = new_message.replace(d, ' ')

    ls = new_message.split()

    # Checking accuracy of the words
    correct = 0
    for word in ls:
        if word in english_vocab \
        or (word[-1] == 's' and word[:-1] in english_vocab) \
        or (word[-2:] == 'ed' and word[:-2] in english_vocab):
            correct = correct + 1

    # Judging the quality of deciphered message
    cur_acc = correct/len(ls)
    if cur_acc > max_acc and cur_acc > accuracy_threshold:
        correct_shift = i
        max_acc = cur_acc
        deciphered_message = new_message

if correct_shift >= 0:
    print(f"\nThe possible deciphered message: \n\n {deciphered_message}\n\n With +{correct_shift} shift(s)")
else:
    print(f"\nCould not decipher the message...")