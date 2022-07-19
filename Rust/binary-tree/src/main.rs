fn hello() {
    println!("hello")
}

fn main() {
    let mut root = Tree {
        value: 1,
        left: Nothing,
    };
    hello();
}

struct Tree {
    value: u8,
    left: Tree,
    right: Tree,
}
