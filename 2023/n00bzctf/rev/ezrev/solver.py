
# for (int i = 0; i < array2.length; ++i) {
#     if (i % 2 == 0) {
#         array2[i] = (char)(array2[i] ^ 0x13);
#     }
#     else {
#         array2[i] = (char)(array2[i] ^ 0x37);
#     }
# }
# for (int j = 0; j < array2.length / 2; ++j) {
#     if (j % 2 == 0) {
#         final int n = array2[j] - 10;
#         array2[j] = (char)(array2[array2.length - 1 - j] + 20);
#         array2[array2.length - 1 - j] = (char)n;
#     }
#     else {
#         array2[j] = (char)(array2[j] + 30);
#     }
# }

flag = [130, 37, 70, 115, 64, 106, 143, 34, 54, 134, 96, 98, 125, 98, 138, 104, 25, 3, 66, 78, 24, 69, 91, 80, 87, 67, 95, 8, 25, 22, 115]

for i in range(len(flag)//2):
  if i%2 == 0:
    n = flag[len(flag) - 1 - i] + 10
    flag[len(flag) - 1 - i] = flag[i] - 20
    flag[i] = n
  else:
    flag[i] -= 30

for i in range(len(flag)):
  if i%2 == 0:
    flag[i] ^= 0x13
  else:
    flag[i] ^= 0x37

for m in flag:
  print(chr(m), end='')
print('')
