#pragma once
#include <stdio.h>
#include <stdlib.h>

typedef struct cell Cell;
struct cell {
  int content;
  Cell* previous;
  Cell* next;
};

typedef struct linked_list List;
struct linked_list {
  Cell* start;
  Cell* end;
  unsigned length;
};

Cell* cell_init(int num);
List* list();
void ordered_insert(List* list, int num);
void list_print(List* list);
void list_destroy(List* list);
