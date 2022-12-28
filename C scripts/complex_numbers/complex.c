#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "complex.h"

Complex *complex_init(float real, float imag)
{
  Complex *c = malloc(sizeof(Complex));
  *c = (Complex){.real = real, .imag = imag};
  return c;
}

void complex_print(Complex* c_num)
{
  char sign = '+';
  if (c_num->imag < 0)
    sign = '-';
  printf("%f%cj%f\n", c_num->real, sign, fabs(c_num->imag));
}
