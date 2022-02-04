#include "abb.h"

ABB* abb_init(long int value) {
  ABB* obj = malloc(sizeof(ABB));
  *obj = (ABB){.left = NULL, .right = NULL, .value = value};
  return obj;
}

void abb_insert(ABB* abb, ABB* insertion) {
  if (insertion->value < abb->value && !abb->left)
    abb->left = insertion;
  else if (insertion->value < abb->value)
    abb_insert(abb->left, insertion);
  else if (!abb->right)
    abb->right = insertion;
  else
    abb_insert(abb->right, insertion);
}

void abb_insert_value(ABB* abb, long int value) {
  ABB* insertion = abb_init(value);
  abb_insert(abb, insertion);
}

void abb_destroy(ABB* abb) {
  if (abb->left)
    abb_destroy(abb->left);
  if (abb->right)
    abb_destroy(abb->right);
  free(abb);
}
