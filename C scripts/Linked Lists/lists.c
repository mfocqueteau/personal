#include "lists.h"

Cell* cell_init(int num) {
  Cell* cell = malloc(sizeof(Cell));
  *cell = (Cell){.content = num, .previous = NULL, .next = NULL};
  return cell;
}

List* list() {
  List* list = malloc(sizeof(List));
  *list = (List) {.start = NULL, .end = NULL, .length = 0};
  return list;
}

void ordered_insert(List* list, int num) {
  Cell* insertion = cell_init(num);
  list->length += 1;
  if (!list->end) {
    list->start = insertion;
    list->end = insertion;
    return;
  }
  if (list->end->content < num) {
    insertion->previous = list->end;
    list->end->next = insertion;
    list->end = insertion;
    return;
  }
  Cell* cursor = list->end;
  while (cursor && cursor->content > num)
    cursor = cursor->previous;
  insertion->previous = cursor;
  if (cursor) {
    insertion->next = cursor->next;
    cursor->next->previous = insertion;
    cursor->next = insertion;
  }
  else {
    insertion->next = list->start;
    list->start = insertion;
  }
  
}

void list_print(List* list) {
  printf("[");
  Cell* cursor = list->start;
  if (cursor) {
    while (cursor->next) {
      printf("%d, ", cursor->content);
      cursor = cursor->next;
    }
    printf("%d", cursor->content);
  }
  printf("]\n");
}

void list_destroy(List* list) {
  Cell* cursor = list->start;
  free(list);
  while (cursor->next) {
    cursor = cursor->next;
    free(cursor->previous);
  }
  free(cursor);
}
