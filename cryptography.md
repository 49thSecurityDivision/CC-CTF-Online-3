# Cryptography

## air raid vehicle
Introducing the ARV hashing algorithm, which is designed to be as lightweight as possible while still delivering irreversible hashing of input of any length.

To put our money where our mouth is, we have hashed a secret and are providing it to you now. Bet you can't reverse it!

We are setting out to prove that there is nothing wrong with rollin' your own crypto!

Note: This flag is not in the flag{...} format, but in a ctf{...} format

file: artifacts/{arv,encrypted_flag.txt}

## smithy
We encrypt messages between admins with our public key, so only our private key can decrypt them. However, we had a super secret declassification process on admin messages so they could be shared with collaborators without exposing flags.

We fired Smithy after sharing too much information with a non-collaborator...

These are the attachments on the email that was the final straw...

NOTE: The flag is not in the flag{...} format, but in the ctf{...} format
file: artifacts/{pub.key,msg.txt,enc_msg.txt}

## new numbers
I wonder what they say...

NOTE: This flag does not follow the flag{...} format, but its does follow a XXX{...} format

file: artifacts/kak.png

## evil eyes

We've come across an exposed testing server. It looks like the developer was trying to allow any user to list the contents of the flag directory, but didn't want to bother with cataloging every possible compilation combination. So, instead, they added their own custom security steps to prevent unauthorized executions.

Based on some testing (which you are free to repeat!), it looks like these are the rules:

- The server accepts any file, but will only execute ELF files
- The server stores the MD5 checksum of the previously approved binary. If your upload's MD5 checksum does not match the stored MD5, then your binary is executed in a controlled environment (firejail, we think) and its result is compared to the "expected result"
- If the result of the execution does not match the "expected result", the binary is discarded and no other operations are performed
- If the result of the execution does match the "expected result", the MD5 checksum is stored, replacing the previous MD5 checksum
- Finally, if you upload any file that matches the currently stored MD5 checksum, it is executed with no restrictions or protections, as it is previously "approved"
There are several ways to obtain the "expected result" and have your program's MD5 checksum become the "accepted" checksum. Below is a program that we know for certain obtains the "expected result" when compiled using gcc with no additional arguments.

```
#include <unistd.h>

int main() {
  char *args[]={"/usr/bin/ls", "./flag", NULL};
  execve("/usr/bin/ls", args, NULL);
}
```
NOTE: The flag is not in the flag{...} format, but in the ctf{...} format

dir: endpoint

## squeeze
We finally found it! The perfect crypto at the lightest weight possible!

We had to squeeze a lot of crypto into a small space for this one!

Hey... wait a minute...

NOTE: This flag is not in the flag{...} format, but in the ctf{...} format

file: artifacts/{output.txt,squeeze}
