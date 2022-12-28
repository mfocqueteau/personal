#include <stdio.h>

#include "node.h"

int main(int argc, char **argv)
{
  if (argc < 2)
  {
    puts("Falta archivo de input");
    return 1;
  }

  FILE *input_data = fopen(argv[1], "r+");
  int n, x, y;
  fscanf(input_data, "%d", &n);

  Node *nodes[n];

  // Leer nodos desde archivo
  for (char i = 0; i < n; i++)
  {
    fscanf(input_data, "%d %d", &x, &y);
    nodes[i] = node__init__(x, y);
  }

  // Liberar memoria
  for (char i = 0; i < n; i++)
    free(nodes[i]);
  fclose(input_data);
  return 0;
}
