#include "valuations.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void next_valuation(Valuation* valuation) {
  char length = strlen(valuation->string);
  char next[length];
  for (char i = length - 1; i >= 0; i--) {
    if (valuation->string[i] == '0') {
      valuation->string[i] = '1';
      break;
    } else
      valuation->string[i] = '0';
  }
}

Valuation* valuation_init(char* string) {
  Valuation* valuation = malloc(sizeof(Valuation));
  valuation->string = string;
  return valuation;
}
