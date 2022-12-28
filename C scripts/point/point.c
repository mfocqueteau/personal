#include <stdio.h>
#include <stdlib.h>

#include "point.h"

Point *point_init(int x, int y)
{
  Point *new_point = malloc(sizeof(Point));
  *new_point = (Point){.x = x, .y = y};
  return new_point;
}

const char *point_str(Point *self)
{
  char *r;
  sprintf(r, "(%d, %d)", self->x, self->y);
  return r;
}
