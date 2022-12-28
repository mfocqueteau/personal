

typedef struct point Point;

struct point
{
  int x;
  int y;
};

Point *point_init(int x, int y);
const char *point_str(Point *self);
