#pragma once

#include <stdio.h>

/* Aliases */
typedef struct tree Tree;
typedef struct queue Queue;
typedef struct qnode QNode;

/* Tree */
struct tree
{
  int value;
  Tree *left;
  Tree *right;
};

Tree *tree_from_file(FILE *file);
Tree *tree_init(int value);
void tree_destroy(Tree *tree);

/* Queue */
struct queue
{
  QNode *start;
  QNode *end;
  unsigned int length;
};

Queue *queue_init();
void append(Queue *queue, Tree *tree);
Tree *popleft(Queue *queue);
void queue_destroy(Queue *queue);

/* QNode */
struct qnode
{
  Tree *tree;
  QNode *next;
  QNode *prev;
};

QNode *_qnode_init(Tree *tree);
void _qnode_destroy(QNode *qnode);
