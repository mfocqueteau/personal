#include <stdio.h>
#include <stdlib.h>

typedef struct abb ABB;
struct abb {
  ABB* left;
  ABB* right;
  long int value;
};

ABB* abb_init(long int value);
void abb_insert(ABB* abb, ABB* insertion);
void abb_insert_value(ABB* abb, long int value);
void abb_destroy(ABB* abb);
