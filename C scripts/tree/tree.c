#include <stdlib.h>

#include "tree.h"

/* Tree */
Tree *tree_init(int value)
{
  Tree *new_tree = malloc(sizeof(Tree));
  *new_tree = (Tree){.value = value, .left = NULL, .right = NULL};
  return new_tree;
}

Tree *tree_from_file(FILE *file)
{
  unsigned n;
  int r;
  fscanf(file, "%u", &n);
  fscanf(file, "%d", &r);

  Tree *root = tree_init(r);
  Queue *queue = queue_init();
  append(queue, root);

  Tree *cur;
  int left, right;
  for (unsigned i = 1; i < n; i += 2)
  {
    fscanf(file, "%d %d", &left, &right);
    printf("%u, %d, %d\n", i, left, right);
    cur = popleft(queue);
    cur->left = tree_init(left);
    cur->right = tree_init(right);
    append(queue, cur->left);
    append(queue, cur->right);
  }

  queue_destroy(queue);

  return root;
}

void tree_destroy(Tree *tree)
{
  if (tree->left != NULL)
    tree_destroy(tree->left);
  if (tree->right != NULL)
    tree_destroy(tree->right);
  free(tree);
}

/* Queue */
Queue *queue_init()
{
  Queue *new_queue = malloc(sizeof(Queue));
  *new_queue = (Queue){.length = 0, .start = NULL, .end = NULL};
  return new_queue;
}

void append(Queue *queue, Tree *tree)
{
  QNode *new_node = _qnode_init(tree);
  if (queue->end == NULL)
    queue->start = new_node;
  else
    queue->end->next = new_node;
  queue->end = new_node;
  queue->length++;
}

Tree *popleft(Queue *queue)
{
  Tree *ret = queue->start->tree;
  free(queue->start);
  printf("%d\n", ret->value);
  queue->start = queue->start->next;
  if (queue->start == NULL)
    queue->end = NULL;
  queue->length--;
  return ret;
}

void queue_destroy(Queue *queue)
{
  if (queue->start != NULL)
    _qnode_destroy(queue->start);
  free(queue);
}

/* QNode */
QNode *_qnode_init(Tree *tree)
{
  QNode *new_qnode = malloc(sizeof(QNode));
  *new_qnode = (QNode){.tree = tree, .next = NULL, .prev = NULL};
  return new_qnode;
}

void _qnode_destroy(QNode *qnode)
{
  if (qnode->next != NULL)
    _qnode_destroy(qnode->next);
  free(qnode);
}
