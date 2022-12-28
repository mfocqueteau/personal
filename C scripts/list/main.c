#include <stdio.h>

char get_bit(int num, char index)
{
  return (num >> index) & 1;
}

int main()
{
  printf("%hu\n", get_bit(21, 1));
  return 0;
}
