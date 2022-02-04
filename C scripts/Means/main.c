#include "means.c"

int main() {
  double my_array[] = {7, 1, 5.5, 4, 5.5, 4, 5.5, 4, 5.5, 7};
  unsigned char length = 8;
  double average = arithmetic(my_array, length);
  printf("Average is %f\n", average);
  // double empty[1] = {3};
  // printf("Empty[0]: %f  %f\n", empty[0], empty[1]);
  printf("Calculated length is %ld\n", get_length(my_array));
  return 0;
}
