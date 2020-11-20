#include "lists.c"

int main() {
  List* myList = list();
  list_print(myList);
  int numbers[] = {7, 3, 1, 2, 5};
  for (char i = 0; i < 5; i++) {
    ordered_insert(myList, numbers[i]);
    list_print(myList);
  }
  list_destroy(myList);
  return 0;
}
