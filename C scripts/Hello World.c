#include <stdio.h>




void guessNumber(int guess) {
    // TODO: write your code here
    if (guess < 555) {
        printf("Your guess is too low");
    } else if (guess == 555) {
        printf("Correct. You guessed it!");
    } else {
        printf("Your guess is too high");
    }
}

int main() {
    char name[] = "Marto";
    printf("%s\n", name);
}