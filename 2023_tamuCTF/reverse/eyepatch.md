# Eyepatch

Reverse Engineering, 500- pts

> Corporate said we were behind schedule, so we pushed our untested code to production. Unfortunately, we realized that we had some unintended bugs in our code. We need you to fix the binary before corporate gets word of this.

The name of the challenge hints at patching binaries. I will use Ghidra to see what is going on with this binary.

## A numerical mistype

Inside the `main` function, there are 3 `printf` lines, corresponding to the 3 values. The first value is `fib(0x20)`. The `fib` function shows a recursive implementation of the Fibonacci sequence:

```c
int fib(int param_1)

{
  int iVar1;
  int iVar2;
  
  if (param_1 == 0) {
    iVar2 = 0;
  }
  else if (param_1 == 1) {
    iVar2 = 2;
  }
  else {
    iVar1 = fib(param_1 + -1);
    iVar2 = fib(param_1 + -2);
    iVar2 = iVar2 + iVar1;
  }
  return iVar2;
}
```

The error here is that `fib(1)` is set to `2`, causing every subsequent value to be doubled. So the first patch would be to change it back to `1`. The address `0x1011a5` holds the value `02`. Change it to `01`.

## A flipped comparison

The next value is `int_relu(0x2a)`, which should print `42`. Looking into the function, we see that the comparison is indeed flipped:

```c
int int_relu(int param_1)

{
  if (-1 < param_1) {
    param_1 = 0;
  }
  return param_1;
}
```

The intended behaviour is to set it to 0 if the number is below 0. Addresses `0x1011d7 - 0x1011dc` holds the comparison instruction, and then `JNS` (jump if not sign). We would like to change this instruction to `JS` (jump if sign), so change the instruction byte `79` to `78`. Then the decompiler shows that we have made the correct change:

```c
int int_relu(int param_1)

{
  if (param_1 < 0) {
    param_1 = 0;
  }
  return param_1;
}
```

# A wrong math operation between two numbers

In the function `det`, we see that it is doing some math operations on an array of `float`s, and returning a float. 

```c
float det(float *param_1)

{
  return param_1[3] * *param_1 + param_1[1] * param_1[2];
}
```

The printed value is higher than the expected output. The inputted array has values `[3, 2, 4, 5]` (as floats), and according to the `det` function, the output is `5 * 3 + 2 * 4 = 23`, exactly what we observed. The expected output is `7 = 5 * 3 - 2 * 4`, which means we need to change the `+` to a `-`.

The assembly instructions contain a single `ADDSS` instruction, which needs to be changed to `SUBSS`. Change the instruction at `0x101180` from `58` to `5c`.

When all is done, export the program in `ELF` format, and submit the binary. (You may run it beforehand to check the result and make sure the binary was not corrupted.)

`gigem{i_hope_you_didnt_pwn_our_infra}`
