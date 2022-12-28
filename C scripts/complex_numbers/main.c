#include <stdio.h>
#include <stdlib.h>

#include "complex.h"

int main()
{
  Complex *my_comp = complex_init(2.617, -3.14159265);

  complex_print(my_comp);

  free(my_comp);
  return 0;
}
