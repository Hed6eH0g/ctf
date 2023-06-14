### EZrev

![EZrev](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/rev/ezrev/ezrev_0.png)

Though there are several famous decompilers, we can employ an online decompiler [here] for an example.
Then, we have the following result and found that the flag was XORed with `0x13` or `0x37` and then, swapped with a few additive operations.
```
import java.util.Arrays;

// 
// Decompiled by Procyon v0.5.36
// 

public class EZrev
{
    public static void main(final String[] array) {
        if (array.length != 1) {
            System.out.println("L");
            return;
        }
        final String s = array[0];
        if (s.length() != 31) {
            System.out.println("L");
            return;
        }
        final int[] array2 = s.chars().toArray();
        for (int i = 0; i < array2.length; ++i) {
            if (i % 2 == 0) {
                array2[i] = (char)(array2[i] ^ 0x13);
            }
            else {
                array2[i] = (char)(array2[i] ^ 0x37);
            }
        }
        for (int j = 0; j < array2.length / 2; ++j) {
            if (j % 2 == 0) {
                final int n = array2[j] - 10;
                array2[j] = (char)(array2[array2.length - 1 - j] + 20);
                array2[array2.length - 1 - j] = (char)n;
            }
            else {
                array2[j] = (char)(array2[j] + 30);
            }
        }
        if (Arrays.equals(array2, new int[] { 130, 37, 70, 115, 64, 106, 143, 34, 54, 134, 96, 98, 125, 98, 138, 104, 25, 3, 66, 78, 24, 69, 91, 80, 87, 67, 95, 8, 25, 22, 115 })) {
            System.out.println("W");
        }
        else {
            System.out.println("L");
        }
    }
}
```

Thus, we can recover the flag by calculating the same operations in the reverse order, and the code for this is as follows:
```
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
```