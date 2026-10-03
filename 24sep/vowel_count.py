with open('info.txt','r') as file1:
    vowel_count = {
        'a' : 0,
        'e' : 0,
        'i' : 0,
        'o' : 0,
        'u' : 0,
    }
    content = file1.read()
    for c in content:
        # match c:
        #     case 'a':
        #         vowel_count['a'] += 1
        #     case 'e':
        #         vowel_count['e'] += 1
        #     case 'i':
        #         vowel_count['i'] += 1
        #     case 'o':
        #         vowel_count['o'] += 1
        #     case 'u':
        #         vowel_count['u'] += 1
        if c in vowel_count:
            vowel_count[c] += 1
    print(vowel_count)

    print("Characters in file:", len(content))
    print("")