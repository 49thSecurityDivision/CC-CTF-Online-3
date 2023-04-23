# pwn

## bin mechanic 0: no entry
Hmmm... Someone has b0rked the entry point... It is supposed to be 0x340804905c

NOTE: Once the file works, obtain the flag with the -c option (the -d option prints a decoy and is an artifact for future challenges).

file: artifacts/bin0

## trash heap: eezy peezy
We came across a company that decided to implement its own heap... Let's break it!

NOTE: The binary was built on a Debian GNU/Linux 11 (bullseye) machine

 nc russian-bot.net 8002

file: artifacts/trash

## bin mechanic 1: crash header
Please don't execute this file as is! The behavior is undefined...

My buddy who uses 64-bit Ubuntu as his OS modified this file to get it past a file parser. Can you change it back?

file: artifacts/bin1

## bin mechanic 2: right in two
Where is the magic?

file: artifacts/bin2

## strings
I once had strings

But now I'm free

There are no strings on me

file: artifacts/strings-file
