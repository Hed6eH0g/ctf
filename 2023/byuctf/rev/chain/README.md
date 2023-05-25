

### Chain

![Chain](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/rev/chain/figs/chain_0.png)

As IDA Free seems not to be supporting the given file format (ELF 32-bit LSB executable, ARM, etc.), open it with Ghidra and look for the main function first.
[Display Function Call Trees] in the toolbar allows us to check for which functions are calling with each other and it was found `FUN_00010520` calles other functions such as `FUN_000106a0` and `FUN_00010958` (see Fig. 1).

Fig. 1
![ghidra-1](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/rev/chain/figs/ghidra_1.png)

In `FUN_000106a0`, one can see that the program (see below) requests to input a password so that the input satisfies `(uint)((byte)FUN_000105ac[*(int *)(&DAT_00021040 + local_1c4 * 4)] ^ abStack_10c[local_1c4]) != (local_1c0[local_1c4] & 0xff)`  for `0 \leq local_1c4 \leq 43`.
```
undefined4 FUN_000106a0(void)

{
  size_t sVar1;
  int iVar2;
  int local_1c4;
  uint local_1c0 [45];
  byte abStack_10c [256];
  int local_c;
  
  local_c = 0;
  memset(local_1c0,0,0xb4);
  local_1c0[0] = 0xc2;
  local_1c0[1] = 0x9c;
  local_1c0[2] = 0x65;
  local_1c0[3] = 0x83;
  local_1c0[4] = 0x95;
  local_1c0[5] = 0x66;
  local_1c0[6] = 0xfa;
  local_1c0[7] = 0x15;
  local_1c0[8] = 0x5e;
  local_1c0[9] = 0x58;
  local_1c0[10] = 0x2f;
  local_1c0[11] = 0x23;
  local_1c0[12] = 0xac;
  local_1c0[13] = 0x4f;
  local_1c0[14] = 0xa1;
  local_1c0[15] = 0x4c;
  local_1c0[16] = 0x7d;
  local_1c0[17] = 0x1e;
  local_1c0[18] = 0x69;
  local_1c0[19] = 0x80;
  local_1c0[20] = 0x8c;
  local_1c0[21] = 0x4a;
  local_1c0[22] = 0x26;
  local_1c0[23] = 0x5b;
  local_1c0[24] = 0x5f;
  local_1c0[25] = 0x91;
  local_1c0[26] = 0x30;
  local_1c0[27] = 0xcf;
  local_1c0[28] = 0xc0;
  local_1c0[29] = 0x4d;
  local_1c0[30] = 0x97;
  local_1c0[31] = 0x9b;
  local_1c0[32] = 0xba;
  local_1c0[33] = 0x20;
  local_1c0[34] = 0x77;
  local_1c0[35] = 0x4c;
  local_1c0[36] = 0xf5;
  local_1c0[37] = 0xef;
  local_1c0[38] = 0x97;
  local_1c0[39] = 0x96;
  local_1c0[40] = 0x31;
  local_1c0[41] = 0x30;
  local_1c0[42] = 0x8c;
  local_1c0[43] = 0xe2;
  puts("Password? ");
  fgets((char *)abStack_10c,0xff,stdin);
  sVar1 = strlen((char *)abStack_10c);
  if (sVar1 == 0x2d) {
    for (local_1c4 = 0; local_1c4 < 0x2c; local_1c4 = local_1c4 + 1) {
      if ((uint)((byte)FUN_000105ac[*(int *)(&DAT_00021040 + local_1c4 * 4)] ^
                abStack_10c[local_1c4]) != (local_1c0[local_1c4] & 0xff)) {
        iVar2 = printf("Wrong!");
        goto LAB_00010914;
      }
    }
    iVar2 = puts("Correct!");
  }
  else {
    iVar2 = puts("Wrong!");
  }
LAB_00010914:
  if (local_c != 0) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(iVar2,local_c,0);
  }
  return 0;
}
```

In the evaluation, `FUN_0001050ac` is used as an array; that is the function and the set of mnemonics there are dealt with as corresponding hex entries in an array (see below).
```
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined FUN_000105ac()
             undefined         r0:1           <RETURN>
                             FUN_000105ac                                    XREF[3]:     thunk_FUN_000105ac:0001060c(T), 
                                                                                          thunk_FUN_000105ac:0001060c(j), 
                                                                                          FUN_000106a0:0001089c(R), 
                                                                                          000210f4(*)  
        000105ac 24 00 9f e5     ldr        r0=>stderr,[->stderr]                            = 000210f8
        000105b0 24 10 9f e5     ldr        r1,[->stderr]                                    = 000210f8
        000105b4 00 30 41 e0     sub        r3,r1,r0
        000105b8 a3 1f a0 e1     mov        r1,r3, lsr #0x1f
        000105bc 43 11 81 e0     add        r1,r1,r3, asr #0x2
        000105c0 c1 10 b0 e1     movs       r1,r1, asr #0x1
        000105c4 1e ff 2f 01     bxeq       lr
        000105c8 10 30 9f e5     ldr        r3,[DAT_000105e0]
        000105cc 00 00 53 e3     cmp        r3,#0x0
        000105d0 1e ff 2f 01     bxeq       lr
        000105d4 13 ff 2f e1     bx         r3
                             PTR_stderr_000105d8                             XREF[1]:     FUN_000105ac:000105ac(R)  
        000105d8 f8 10 02 00     addr       stderr
                             PTR_stderr_000105dc                             XREF[1]:     FUN_000105ac:000105b0(R)  
        000105dc f8 10 02 00     addr       stderr
                             DAT_000105e0                                    XREF[1]:     FUN_000105ac:000105c8(R)  
        000105e0 00 00 00 00     undefined4 00000000h

```

Since `DAT_00021040` holds the following values (column having `0Eh, 00h, ...`) what does the condition evaluate for an input can be illustrated as shown in Fig. 3.
```
                             DAT_00021040                                    XREF[2]:     FUN_000106a0:00010894(R), 
                                                                                        00010950(*)  
        00021040 0e              ??         0Eh
        00021041 00              ??         00h
        00021042 00              ??         00h
        00021043 00              ??         00h
        00021044 03              ??         03h
        00021045 00              ??         00h
        00021046 00              ??         00h
```

Fig. 3
![array structure](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/rev/chain/figs/array_structure.png)

Therefore, we made a python script to recover the flag by xoring `(uint)((byte)FUN_000105ac[*(int *)(&DAT_00021040 + local_1c4 * 4)]` with `local_1c0` as follows:
```
local_1c0 = [0xc2, 0x9c, 0x65, 0x83, 0x95, 0x66, 0xfa, 0x15, 0x5e, 0x58, 0x2f, 0x23, 0xac, 0x4f, 0xa1, 0x4c, 0x7d, 0x1e, 0x69, 0x80, 0x8c, 0x4a, 0x26, 0x5b, 0x5f, 0x91, 0x30, 0xcf, 0xc0, 0x4d, 0x97, 0x9b, 0xba, 0x20, 0x77, 0x4c, 0xf5, 0xef, 0x97, 0x96, 0x31, 0x30, 0x8c, 0xe2]    

dat_00021040 = [0x0E, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x1C, 0x00, 0x00, 0x00, 0x13, 0x00, 0x00, 0x00, 0x17, 0x00, 0x00, 0x00, 0x21, 0x00, 0x00, 0x00, 0x12, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x27, 0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x0D, 0x00, 0x00, 0x00, 0x22, 0x00, 0x00, 0x00, 0x1E, 0x00, 0x00, 0x00, 0x15, 0x00, 0x00, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x24, 0x00, 0x00, 0x00, 0x1D, 0x00, 0x00, 0x00, 0x0A, 0x00, 0x00, 0x00, 0x18, 0x00, 0x00, 0x00, 0x2B, 0x00, 0x00, 0x00, 0x19, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1B, 0x00, 0x00, 0x00, 0x2A, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x1F, 0x00, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x25, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x1A, 0x00, 0x00, 0x00, 0x0C, 0x00, 0x00, 0x00, 0x29, 0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x11, 0x00, 0x00, 0x00, 0x28, 0x00, 0x00, 0x00, 0x14, 0x00, 0x00, 0x00, 0x16, 0x00, 0x00, 0x00, 0x23, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x2C, 0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x26, 0x00, 0x00, 0x00]


FUN_000105ac = [0x24, 0x00, 0x9f, 0xe5,0x24, 0x10, 0x9f, 0xe5,0x00, 0x30, 0x41, 0xe0,0xa3, 0x1f, 0xa0, 0xe1,0x43, 0x11, 0x81, 0xe0,0xc1, 0x10, 0xb0, 0xe1,0x1e, 0xff, 0x2f, 0x01,0x10, 0x30, 0x9f, 0xe5,0x00, 0x00, 0x53, 0xe3,0x1e, 0xff, 0x2f, 0x01,0x13, 0xff, 0x2f, 0xe1, 0xf8, 0x10, 0x02, 0x00, 0xf8, 0x10, 0x02, 0x00]

flag = ''
for local_1c4 in range(0x2c):      
  FUN_000105ac_index = dat_00021040[local_1c4 * 4]
  flag += chr(((FUN_000105ac[FUN_000105ac_index]) ^ local_1c0[local_1c4]) & 0xff)

print(flag)
```
