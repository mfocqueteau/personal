#include "looper.c"

int main() {
  StrLooper* my_loop = str_looper("String de Prueba");
  for (char i = 0; i < 33; i++)
    printf("%c\n", str_next(my_loop));
  printf("\n");
  free_str_looper(my_loop);
  return 0;
}
