#include <unistd.h>

int main() {
  char *args[]={"/usr/bin/cat", "./flag/flag.txt", NULL};
  execve("/usr/bin/cat", args, NULL);
}
