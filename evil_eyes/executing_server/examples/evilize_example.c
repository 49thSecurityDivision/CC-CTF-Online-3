#include <unistd.h>
#include <stdio.h>

int main_good() {
  char *args[]={"/usr/bin/ls", "./flag", NULL};
  execve("/usr/bin/ls", args, NULL);
}

int main_evil() {
  char *args[]={"/usr/bin/cat", "./flag/flag.txt", NULL};
  execve("/usr/bin/cat", args, NULL);
}
