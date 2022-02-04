#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct looper {
  unsigned int cursor;
  unsigned int length;
} Looper;

Looper* looper(unsigned int length);
unsigned int next(Looper* loop_obj);

typedef struct str_loop {
  Looper* looper;
  char* string;
} StrLooper;

StrLooper* str_looper(char* string);
char str_next(StrLooper* loop_obj);
void free_str_looper(StrLooper* loop_obj);
