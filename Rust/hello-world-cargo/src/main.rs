// Constantes
const CONSTANT: u8 = 13;

// enum Direction {
//     Up,
//     Down,
// }

fn main() {
    println!("The value of constant CONSTANT is: {}", CONSTANT);

    // Variables
    let c: i8 = -17;
    println!("The value of inmutable variable c is: {}", c);
    let mut v: i8 = -128;
    println!("The value of mutable variable v is: {}", v);
    v = 68;
    println!("The new value of mutable variable v is: {}", v);

    // Conrol de flujo
    if v < 68 {
        println!("v is less than 68");
    } else if v > 68 {
        println!("v is more than 68");
    } else {
        println!("v is equal to 68");
    }

    let mut n: u8 = 0;
    loop {
        n += 1;
        if n == 2 {
            continue;
        }
        if n > 4 {
            break;
        }
        println!("The value of n is: {}", n);
    }

    n = 1;
    while n <= 4 {
        println!("The value of n is: {}", n);
        n += 1;
    }

    // let range = 1..5;  // No descomentar
    // let animals = vec!["Rabbit", "Dog", "Cat"];

    // for (i, a) in animals.iter().enumerate() {
    //     println!("{}. The animal is: {}", i, a);
    // }

    // let player_direction: Direction = Direction::Up;

    // match player_direction {
    //     Direction::Up => println!("Moving up!"),
    //     Direction::Down => println!("Moving down")
    // }

    // Tuplas
    let tup1: (u8, bool, f32, &str) = (20, false, 3.1415, "Rust");
    println!("{}", tup1.2);
}
