#include <stdio.h>

// variabili globali
int gg = 10;

// funzione di base
int sum(int a, int b) {
    int c = a + b;
    return c;
}

// funzione di test "incremento"
void incr(void) {
    gg = gg + 1;
    printf("Valore di \"gg\": %d\n", gg);
}
// funzione di test con ritorno di un valore
int incr_bis(int x) {
    x = x+1;
    return x;
}

int main(void) {

    // print con funzione puts
    puts("Programma con puts invece di printf");

    // test della funzione somma usando %d per stampare un intero
    printf("Test della funzione somma (sum): %d\n", sum(10, 10));

    // test della funzione variatica printf
    // printf("Test: passo a printf solo un decimale ma ne prevedo due: %d %d\n", 6);

    // test della funzione incremento che usa una variabile globale
    incr(); incr(); incr();

    // test della funzione incr_bis
    printf("La funzione incr_bis() con parametro 5 ritorna %d\n", incr_bis(5));

    return 0;
}