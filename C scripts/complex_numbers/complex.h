#pragma once

typedef struct complex Complex;

struct complex
{
  float real;
  float imag;
};

Complex *complex_init(float real, float imag);
void complex_print(Complex* c_num);
