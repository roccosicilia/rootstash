#include <stdio.h>
#include <limits.h>

int main() {

    // variabili locali
    int a = 10;
    float b = 1.1;

    // altri tipi di variabili
    char c = 127;

    //print dele variabili
    printf("Valore decimale di a: %d\n", a);
    printf("Valore float di b: %f\n", b);

    //print di un char offsettato
    c++;
    printf("Valore char di c: %c\n", c);

    // dimensione del tipo intero nel mio sistema
    // %lu sta per "long unsigned" che è il tipo di dato di sizeof
    printf("Dimensione del tipo int: %lu bytes\n", sizeof(a));

    // instroduco le costanti di limits.h
    printf("Valore massimo di int: %d\n", INT_MAX);
    printf("Valore minimo di int: %d\n", INT_MIN);
    
    return 0;
} 
