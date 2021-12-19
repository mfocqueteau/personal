#include "valuations.c"

int main() {
  Valuation* val = valuation_init("0000");
  printf("holaaaa\n");
  next_valuation(val);
  printf("%s\n", val);
  return 0;
}
