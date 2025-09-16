#include <iostream>
#include <string>
#include <cmath>

int main() {

    //variabili
    int base;
    int risultato;

    // calcolo il cubo
    std::cout << "Inserisci un numero intero di cui calcolare il cubo: ";
    std::cin >> base;
    risultato = std::pow(base, 3);
    std::cout << "Il cudo di " << base << " è uguale a " << risultato << " \n";
    
    return 0;

}