#include "abb.c"

int main(int argc, char* argv[]) {
  char middle = 3;
  if (argv[1])
    middle = atoi(argv[1]);
  printf("Creando árbol con raíz %hhu...\n", middle);
  ABB* tree = abb_init(middle);
  for (char i = 0; i < middle; i++) {
    abb_insert_value(tree, i);
    abb_insert_value(tree, 2 * middle - i);
  }
  abb_destroy(tree);
  return 0;
}
