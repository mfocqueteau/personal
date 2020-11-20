#include <stdio.h>
#include <stdlib.h>


long unsigned int factorial(long unsigned int);

int main(int argc, char** argv) {
    if (argc != 2) {
        printf("Modo de uso: ./factorial <num>\n");
        return 1;
    }
    long unsigned int query;

    sscanf(argv[1], "%lu", &query);
    long unsigned int result = factorial(query);
    printf("Factorial de %lu es %lu (%ld)\n", query, result, sizeof(result));

    return 0;
}

long unsigned int factorial(long unsigned int number) {
    if (number < 0) return 0;
    if (number == 0) return 1;
    return factorial(number - 1) * number;
}
