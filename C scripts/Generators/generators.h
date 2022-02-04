#pragma once
#include <stdio.h>
#include <stdlib.h>

typedef struct gen_fibonacci Fibo;
struct gen_fibonacci {
  unsigned a;
  unsigned b;
};

typedef struct gen_factorial Factorial;
struct gen_factorial {
  unsigned iteration;
  unsigned result;
};

typedef struct gen_palabra Palabra;
struct gen_palabra {
  char* palabra;
};

/* Fibonacci */
Fibo* fibo_init();
unsigned next_fibo(Fibo* generator);

/* Factorial */
Factorial* factorial_init();
unsigned next_factorial(Factorial* generator);

/* Palabras bits */
Palabra* palabra_init();
char* next_palabra(Palabra* generator);
