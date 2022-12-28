#include "node.h"

Node *node__init__(int x, int y)
{
  Node *new_node = malloc(sizeof(Node));
  *new_node = (Node){.x = x, .y = y};
  return new_node;
}

int manhattan(Node *n1, Node *n2)
{
  return abs(n1->x - n2->x) + abs(n1->y - n2->y);
}
