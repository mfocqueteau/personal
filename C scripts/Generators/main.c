#include "generators.c"

char* main(int argc, char** argv) {
  char limit = 6;
  Fibo* myFibo = fibo_init();
  Factorial* myFacto = factorial_init();

  printf("%12s%12s\n", "Fibonacci", "Factorial");
  for (unsigned i = 1; i <= limit; i++) {
    printf("%12u", next_fibo(myFibo));
    printf("%12u", next_factorial(myFacto));
    printf("\n");
  }

  free(myFibo);
  free(myFacto);
  return 0;
}
