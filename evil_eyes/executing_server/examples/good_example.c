#include <unistd.h>

int main() {
  char *args[]={"/usr/bin/ls", "./flag", NULL};
  execve("/usr/bin/ls", args, NULL);
}
