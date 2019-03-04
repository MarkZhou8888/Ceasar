def encryption(letter, s):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)
    num_hash = {}
    alpha_hash = {}
    count = 1
    for x in range(len(alpha)):
        num_hash[x+1] = alpha[x]
    for y in alpha:
        alpha_hash[y] = count
        count += 1

    word = list(letter)
    newword = []

    for letter in word:
        if letter in alpha:
            position = alpha_hash[letter]
            position += s
            if position > 26:
                position -= 26
                newletter = num_hash[position]
                newword.append(newletter)
            else:
                newletter = num_hash[position]
                newword.append(newletter)
        else:
            newword.append(letter)

    print(''.join(newword))

encryption("wow", 6)

def decrypt(letter, s):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)
    num_hash = {}
    alpha_hash = {}
    count = 1
    for x in range(len(alpha)):
        num_hash[x+1] = alpha[x]
    for y in alpha:
        alpha_hash[y] = count
        count += 1


    word = list(letter)
    newword = []

    for letter in word:
        if letter in alpha:
            position = alpha_hash[letter]
            position -= s
            if position < 0:
                position += 26
                newletter = num_hash[position]
                newword.append(newletter)
            else:
                newletter = num_hash[position]
                newword.append(newletter)
        else:
            newword.append(letter)

    print(''.join(newword))


decrypt("cuc", 6)
