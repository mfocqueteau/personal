#include "generators.h"

Fibo* fibo_init() {
  Fibo* generator = malloc(sizeof(Fibo));
  *generator = (Fibo){.a = 0, .b = 1};
  return generator;
}

unsigned next_fibo(Fibo* generator) {
  unsigned temp = generator->a;
  generator->a = generator->b;
  generator->b = temp + generator->b;
  return temp;
}

Factorial* factorial_init() {
  Factorial* generator = malloc(sizeof(Factorial));
  *generator = (Factorial){.iteration = 0, .result = 1};
  return generator;
}

unsigned next_factorial(Factorial* generator) {
  generator->iteration++;
  generator->result *= generator->iteration;
  return generator->result;
}
