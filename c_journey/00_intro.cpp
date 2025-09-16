#include <iostream>
#include <string>

/************************************************
* C++ test program
* Author: Rocco Sicilia
* Notes: C++ learning journey
************************************************/

// includere un namespace per evitare di scrivere std:: ogni volta
// using namespace std;

// constanti
const float PI_GRECO = 3.14; // costante, per convenzione in maiuscolo
const int ETA_MASSIMA = 120; // costante

int funzione_di_test(int anno_corrente, int eta) {
    // calcolo la data di nascita
    int anno_di_morte;
    std::cout << "Inserisci la tua età: ";
    anno_di_morte = anno_corrente - eta + ETA_MASSIMA; // calcolo l'anno
    return anno_di_morte;
}

// funzione principale
int main() {
    // variabili
    int anno_di_nascita, anno_corrente, eta;
    int anno_di_morte;
    std::string nome_utente;
    std::string profili[5]; // array di stringhe

    // esecuzione del programma base
    std::cout << "##################################################\n";
    std::cout << "C++ test program\n"; // scrivo a video
    std::cout << "/* */ questa sintassi inserisce un commento\n"; // scrivo a video
    std::cout << "##################################################\n";

    // esempio di input
    std::cout << "Inserisci il tuo anno di nascita: ";
    std::cin >> anno_di_nascita; // leggo da tastiera
    std::cout << "Inserisci l'anno corrente: ";
    std::cin >> anno_corrente; // leggo da tastiera
    eta = anno_corrente - anno_di_nascita; // calcolo l'età
    std::cout << "La tua età è: " << eta << " anni\n";

    // esempio di input per funzione
    anno_di_morte = funzione_di_test(anno_corrente, eta);
    std::cout << "Il tuo anno di morte è: " << anno_di_morte << "\n";

    // esempio di input stringa
    std::cout << "Inserisci il tuo nome: ";
    std::cin >> nome_utente; // leggo da tastiera
    std::cout << "Ciao " << nome_utente << ", piacere di conoscerti!\n";

    // ciclo for per array
    std::cout << "Inserisci 5 profili di social media:\n";
    for (int i = 0; i < 5; i++) {
        std::cout << "Inserisci il profilo " << (i + 1) << ": ";
        std::cin >> profili[i]; // leggo da tastiera
    }
    std::cout << "I profili inseriti sono:\n";
    for (int i = 0; i < 5; i++) {
        std::cout << profili[i] << "\n"; // scrivo a video
    }

    return 0;
}