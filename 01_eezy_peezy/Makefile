CC = gcc

#CFLAGS = -Wall -Wextra -g -m32 -O2 -fno-stack-protector -static
CFLAGS = -g -m32 -fno-stack-protector -static

trash_heap: trash_heap.c
	@$(CC) $(CFLAGS) -o trash trash_heap.c

clean:
	@$(RM) trash
