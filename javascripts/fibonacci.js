class gen_fibonacci {
  constructor() {
    let a = 0;
    let b = 1;
  }
  next() {
    temp = a;
    a = b;
    b += temp;
    return a;
  }
}

FIBO = gen_fibonacci()
