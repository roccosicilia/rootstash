#include <stdio.h>

// funzione di base
int sum(int a, int b) {
    int c = a + b;
    return c;
}

int main(void) {
    // print con funzione puts
    puts("Programma con puts invece di printf");
    // test della funzione somma usando %d per stampare un intero
    printf("Test della funzione somma (sum): %d\n", sum(10, 10));
    // test della funzione variatica printf
    printf("Test: passo a printf solo un decimale ma ne prevedo due: %d %d\n", 6);
    
    
    
    return 0;
}