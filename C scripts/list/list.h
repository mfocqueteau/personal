#include <stdio.h>
#include <stdlib.h>

// Renombramiento de estructuras
typedef struct node node;
typedef struct list list;

struct node
{
  node *prev;
  node *next;
  void *content;
};

struct list
{
  node *start;
  node *end;
  unsigned int length;
};

list *list_init();
void *pop(list *obj);
void *popleft(list *obj);
void list_print(list *obj);
