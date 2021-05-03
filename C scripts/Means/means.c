#include "means.h"

double arithmetic(double* numbers_array, unsigned length) {
  double sum = 0;
  for (unsigned i = 0; i < length; i++) {
    sum += numbers_array[i];
  }
  return sum / length;
}

size_t get_length(void* array) {
  size_t length = sizeof(array) / sizeof(array[0]);
  printf("%ld  %ld\n", sizeof(array), sizeof(array[0]));
  return length;
}
