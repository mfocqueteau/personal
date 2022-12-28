#pragma once

#include <stdlib.h>

typedef struct node Node;
typedef struct edge Edge;

struct node
{
  int x;
  int y;
};

Node *node__init__(int x, int y);
int manhattan(Node *n1, Node *n2);
char *node__str__(Node *node);

struct edge
{
  Node *node1;
  Node *node2;
  int value;
};
