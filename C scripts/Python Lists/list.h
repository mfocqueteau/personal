#include <stdio.h>

unsigned char TYPES[] = {};

typedef struct node Node;
struct node {
  void* content;
  unsigned char type;
  Node* next;
};

typedef struct list list;
struct list {
  Node* root;
  unsigned length;
};
