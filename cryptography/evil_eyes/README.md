# Category

`cryptography`

# Prompt

We've come across an exposed testing server. It looks like the developer was trying to allow any user to list the contents of the flag directory, but didn't want to bother with cataloging every possible compilation combination. So, instead, they added their own custom security steps to prevent unauthorized executions.

Based on some testing (which you are free to repeat!), it looks like these are the rules:

1. The server accepts any file, but will only execute ELF files
2. The server stores the MD5 checksum of the previously approved binary. If your upload's MD5 checksum does not match the stored MD5, then your binary is executed in a controlled environment (firejail, we think) and its result is compared to the "expected result"
3. If the result of the execution does not match the "expected result", the binary is discarded and no other operations are performed
4. If the result of the execution does match the "expected result", the MD5 checksum is stored, replacing the previous MD5 checksum
5. Finally, if you upload any file that matches the currently stored MD5 checksum, it is executed with no restrictions or protections, as it is previously "approved"

There are several ways to obtain the "expected result" and have your program's MD5 checksum become the "accepted" checksum. Below is a program that we know for certain obtains the "expected result" when compiled using gcc with no additional arguments.

```
#include <unistd.h>

int main() {
  char *args[]={"/usr/bin/ls", "./flag", NULL};
  execve("/usr/bin/ls", args, NULL);
}
```

NOTE: The flag is not in the flag{...} format, but in the ctf{...} format

`http://russian-bot.net:1337`