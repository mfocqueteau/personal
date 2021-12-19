#include "looper.h"

Looper* looper(unsigned int length) {
  Looper* loop_obj = malloc(sizeof(Looper));
  loop_obj->cursor = 0;
  loop_obj->length = length;
  return loop_obj;
}

unsigned int next(Looper* loop_obj) {
  unsigned int yield = loop_obj->cursor;
  loop_obj->cursor = (loop_obj->cursor + 1) % loop_obj->length;
  return yield;
}

StrLooper* str_looper(char* string) {
  StrLooper* loop_obj = malloc(sizeof(StrLooper));
  loop_obj->looper = looper(strlen(string));
  loop_obj->string = string;
  return loop_obj;
}

char str_next(StrLooper* loop_obj) {
  char index = next(loop_obj->looper);
  return loop_obj->string[index];
}

void free_str_looper(StrLooper* loop_obj) {
  free(loop_obj->looper);
  free(loop_obj);
}
