class gen_fibonacci {
	constructor() {
		let a = 0;
		let b = 1;
	}
}

function next(gen) {
  temp = gen.a;
  gen.a = gen.b;
  gen.b += temp;
  return gen.a;
}

FIBO = new gen_fibonacci();

console.log(next(FIBO), FIBO.a, FIBO);

