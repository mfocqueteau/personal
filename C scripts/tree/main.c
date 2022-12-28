#include <stdio.h>

#include "tree.h"

int main(int argc, char **argv)
{
  if (argc != 2)
  {
    puts("Uso: ./main <tree_file>.txt");
    return 1;
  }

  FILE *file = fopen(argv[1], "r");
  Tree *root = tree_from_file(file);
  fclose(file);

  tree_destroy(root);
  return 0;
}
