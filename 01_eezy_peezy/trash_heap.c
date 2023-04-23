#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>

#define n 10
#define page_size 4096

struct HeapPage {
  int   size;    // How big is it?
  int   in_use;  // Is it in use?
  int*  next;
  char  content[page_size - (sizeof(int) * 3)]; // What does it point to?
};

struct HeapPage HEAP[n + 1];
int heap_page_count = 0;

void init_the_bloody_heap() {
  FILE* f;
  char* flag = (char*)malloc(100);
  int size = page_size * (n + 1);
  int* heap_base = mmap((void*)0x800000, size, PROT_EXEC | PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
  if ((int)heap_base == -1) {
    printf("Error\n");
    printf("%s\n", strerror(errno));
    exit(1);
  }
  for (int i = 0; i < n; i++) {
    if (i == 0) {
      HEAP[i].next = heap_base + (page_size * (n - 1));
    } else if (i == (n - 1)) {
      HEAP[i].next = heap_base;
    } else {
      HEAP[i].next = heap_base + (page_size * (i - 1));
    }
    HEAP[i].in_use = 0;
    HEAP[i].size = sizeof(HEAP[i].content);
    memset(HEAP[i].content, '\0', sizeof(HEAP[i].content));
  }

  // Handle admin block
  HEAP[n].in_use = 1;
  HEAP[n].size = sizeof(HEAP[n].content);
  memset(HEAP[n].content, '\0', HEAP[n].size);

  f = fopen("./flag.txt", "r");
  fscanf(f, "%s", flag);
  fclose(f);

  strcpy(HEAP[n].content, flag);
  HEAP[n].size = strlen(HEAP[n].content);
}

int allocate() {
  for (int i = 0; i < n; i++) {
    if (HEAP[i].in_use == 0) {
      HEAP[i].in_use = 1;
      memset(HEAP[i].content, '\0', HEAP[i].size);
      printf("Heap block %d allocated...\n", i);
      return n;
    } else if (i == (n - 1)) {
      printf("Heap is full... Start deleting blocks...\n");
      return -1;
    }
  }

  return -1;
}

void deallocate(int block) {
  if (block >= n) {
    printf("\nThat don't make sense...\n");
    exit(1);
  }

  if (HEAP[block].in_use == 0) {
    printf("\nThat block isn't allocated...\n");
  } else {
    HEAP[block].in_use = 0;
    printf("\nHeap block %d freed!\n", block);
  }
}

void list() {
  int found = 0;
  printf("\n");
  for (int i = 0; i < n; i++) {
    if (HEAP[i].in_use == 1) {
      printf("Heap block %d is in use!\n", i);
      found = 1;
    }
  }

  if (!found) {
    printf("No heap blocks allocated!\n");
  }
}

void write_block(int block) {
  int size = page_size * 2;
  char* input = malloc(size);
  memset(input, '\0', size);

  printf("\nWhat would you like to write?\n");
  scanf("%s", input);

  printf("sizeof input:   %ld\n", strlen(input));
  printf("sizeof content: %ld\n", sizeof(HEAP[block].content));
  strcpy(HEAP[block].content, input);
}

void view_block(int block) {
  if (block >= n) {
    printf("That heap block does not exist...\n");
    return;
  }
  if (HEAP[block].in_use == 0) {
    printf("\nHeap block not in use...\n");
    return;
  }

  printf("\nDetails of block %d:\n", block);
  printf("Size:   %d\n", HEAP[block].size);
  printf("In Use: %d\n", HEAP[block].in_use);
  printf("\nContent:\n");
  for (int i = 0; i < HEAP[block].size; i++) {
    printf("%c", HEAP[block].content[i]);
  }
  printf("\n");

  return;
}

int menu() {
  int choice = 999;
  int index = 0;
  char* input;
  char* output;
  int result = 0;

  printf("\n========================================\n");
  printf("========================================\n");
  printf("Welcome to the Trash Heap!\n\n");

  printf("1. Allocate memory on the heap\n");
  printf("2. Free memory from the heap\n");
  printf("3. List blocks in use\n");
  printf("4. Write data to a heap block\n");
  printf("5. View a heap block\n");
  printf("========================================\n");
  printf("========================================\n\n");

  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  scanf("%d", &choice);

  switch(choice) {
    case 1:
      printf("\nAllocating a heap block...\n");
      result = allocate();
      if (result == -1) {
        printf("Something went wrong...\n");
        exit(1);
      }
      break;
      ;;
    case 2:
      printf("\nStarting from 0 (0 is the first block), which block would you like to free?\n");
      scanf("%d", &result);
      deallocate(result);
      break;
      ;;
    case 3:
      printf("\nBlocks in use are...\n");
      list();
      break;
      ;;
    case 4:
      printf("\nWhich block would you like to write to?\n");
      printf("Blocks in use are:\n");
      list();
      scanf("%d", &result);
      write_block(result);
      break;
      ;;
    case 5:
      printf("\nWhich block would you like to view?\n\n");
      scanf("%d", &result);
      view_block(result);
      break;
      ;;
    case 6:
      printf("\nGoodbye\n");
      return 1;
      ;;
    default:
      printf("\nI'm afraid I can't do that, Dave...\n");
      return 1;
  }

  return 0;
}

int main(int argc, char** argv) {
  init_the_bloody_heap();
  int ext = 0;
  while (ext != 1) {
    sleep(1 / 2);
    ext = menu();
  }
}
