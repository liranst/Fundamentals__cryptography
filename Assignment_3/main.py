from auxiliary_functions import *
incidences = "The frequency of the alphabet.csv"
# Open the frequency table
frequency_table = open_file_incidences(incidences)
####################################################
#              Y_affine_cipher                     #
####################################################
# File paths
y1 = "Y_affine_cipher.txt"
# Read the encrypted text
text = open_file(y1)
# Try to identify if 'THE' is present in the text using specified step values
x = maybe_is_The(text, 3, 5)
character_count = count_cher_in_text(text)
incidence_info = info(character_count, frequency_table, visualization=True)
# Decrypt the text using affine cipher with parameters (17, 5)
"""
[1]  21 = 4a + b
[2]  20 = 7a + b    // + 1
[2]  21 = 7a + b + 1
4a = 7a + 1
-3a = 1 --> a = 17
21 = 16 + b 
21 - 16 = b
    || 
    ||
    \/
a = 17 and b = 5 
"""
save_decrypted_text(text, (17, 5), 'X_affine_cipher.txt')
####################################################
#               Y_substitution_cipher              #
####################################################
y2 = "Y_substitution_cipher.txt"
text2 = open_file(y2)
count_cher2 = count_cher_in_text(text2)
info_incidence = info(count_cher2, frequency_table)
"""
in this text there are 3 letters that did not appear at all.
Therefore, 23 letters must be arranged.
According to the frequency table table I think it is
x,y and z.
"""
# maybe_The = maybe_is_The(text2, size=3, top_num=3)
# print(maybe_The)
# output:
# TGK    5
# KQM    5
# CMY    4
# K appears the most times,
# so with a high probability I am sure it is K --> E
# I will therefore change the word according to the percentages
# TGK --> THE
# x,y and z
# thinking = {"T": "T",
#      "G": "H",
#      "K": "E",
#      }
# I checked what the longest substring word is
# maybe_The = maybe_is_The(text2, size=9, top_num=3)
# print(maybe_The)
# GKOSYYMNK    3
# TGKOSYYMN    3
# KQMCMYLVN    2
#
# real_time = list(info_incidence[0])
# percent = list(info_incidence[1])
# k_pi = dict(zip(real_time, percent))
# axaa = ""
# for char in text2:
#     if char in X.keys():
#         axaa += X[char]
#     else:
#         axaa += char
# print(axaa)
# y_k0 = real_time[0:7]
# y_v0 = percent[0:7]
# y_k1 = real_time[7:11]
# y_v1 = percent[7:11]
# y_k2 = real_time[11:22]
# y_v2 = percent[11:22]
# import random
# x = [[y_k0, y_v0],
#      [y_k1, y_v1],
#      [y_k2, y_v2]]
# for i in range(1):
#     random.shuffle(x[0][0])
#     random.shuffle(x[0][1])
#     x1 = dict(zip(x[0][0], x[0][1]))
#
#     random.shuffle(x[1][0])
#     random.shuffle(x[1][1])
#     x2 = dict(zip(x[1][0], x[1][1]))
#
#     random.shuffle(x[2][0])
#     random.shuffle(x[2][1])
#     x3 = dict(zip(x[2][0], x[2][1]))
#     strrr = ""
#     for char in text2:
#         if char in x1.keys():
#             strrr += x1[char]
#         if char in x2.keys():
#             strrr += x2[char]
#
#         if char in x3.keys():
#             strrr += x3[char]
#     if strrr[:3] == "THE":
#         print(strrr)
#         print()
# After much trial and error I arrived at the correct arrangement
mydict = {'B': 'w',
          'C': 'n',
          'E': 'j',
          'F': 'u',
          'G': 'h',
          'H': 'd',
          'I': 'b',
          'K': 'e',
          'L': 'm',
          'M': 'a',
          'N': 'g',
          'O': 'v',
          'P': 'y',
          'Q': 'r',
          'R': 'z',
          'S': 'i',
          'T': 't',
          'U': 'p',
          'V': 'o',
          'W': 'c',
          'X': 'f',
          'Y': 'l',
          'Z': 's'}
x_text2 = ''.join([mydict[char] for char in text2])
print(f"Decrypted text y2:\n{x_text2}")
with open('X_substitution_cipher.txt', 'w', encoding='utf-8') as f:
    f.write(x_text2)