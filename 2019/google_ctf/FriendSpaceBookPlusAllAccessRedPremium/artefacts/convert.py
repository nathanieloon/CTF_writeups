# convert emojis to text
# with open('emojis.txt', 'r', encoding="utf-8") as f:
#     line = f.readline()
#     print(repr(line))
#     while line:
#         line = f.readline

#         print(repr(line))

OPERATIONS = {
    '🍡': 'add',
    '🤡': 'clone',
    '📐': 'divide',
    '😲': 'if_zero',
    '😄': 'if_not_zero',
    '🏀': 'jump_to',
    '🚛': 'load',
    '📬': 'modulo',
    '⭐': 'multiply',
    '🍿': 'pop',
    '📤': 'pop_out',
    '🎤': 'print_top',
    '📥': 'push',
    '🔪': 'sub',
    '🌓': 'xor',
    '⛰': 'jump_top',
    '⌛': 'exit'
}

import codecs
f = codecs.open('emojis.txt', encoding='utf-8')
f2 = codecs.open('output.txt', encoding='utf-8', mode='w')
for line in f:
    for char in line:
        if char in OPERATIONS.keys():
            f2.write(OPERATIONS.get(char))
        else:
            # print(char)
            if char == '0️⃣':
                f2.write(str(ord(char) - ord("0")))
            else:
                f2.write(char)
    f2.write("\n")
    # print(repr(line))
f.close()
f2.close()