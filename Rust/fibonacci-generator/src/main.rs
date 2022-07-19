fn main() {
    let mut fib = FiboGenerator { a: 0, b: 1 };
    for _ in 0..10 {
        println!("{}", fib.next())
    }
}

struct FiboGenerator {
    a: u16,
    b: u16,
}

impl FiboGenerator {
    fn next(&mut self) -> u16 {
        let temp = self.a;
        self.a = self.b;
        self.b += temp;
        return temp;
    }

    fn* iter(&mut self, iterations: u8) {
        for _ in 0..iterations {
            yield self.next()
        }
    }
}
