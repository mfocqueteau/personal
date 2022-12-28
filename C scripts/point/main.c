#include <stdio.h>
#include <stdlib.h>

#include "point.h"

int main()
{
  Point *my_point = point_init(2, -3);

  printf("%s\n", point_str(my_point));
  // point_str(my_point);

  free(my_point);
  return 0;
}
