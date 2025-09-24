#include <iostream>
#include <string>
#include <memory>
#include <vector>

// ---- Klase za primjer ----

// Kompozicija: Motor je sastavni dio Automobila.
// Kad se Automobile uništi, uništi se i Motor.
class Motor {
public:
    Motor(int snaga) : snaga_(snaga) {}
    void pokreni() const { std::cout << "Motor snage " << snaga_ << " kW je pokrenut.\n"; }
private:
    int snaga_;
};

class Automobil {
public:
    Automobil(const std::string& model, int snagaMotora)
        : model_(model), motor_(snagaMotora) {}   // Motor je član po vrednosti

    void start() {
        std::cout << "Automobil " << model_ << " startuje.\n";
        motor_.pokreni();
    }

private:
    std::string model_;
    Motor motor_;   // kompozicija
};

// Agregacija: Vozač može da vozi različite automobile,
// a automobil može da postoji i bez konkretnog vozača.
class Vozac {
public:
    Vozac(const std::string& ime) : ime_(ime) {}

    void dodajAuto(std::shared_ptr<Automobil> autoPtr) {
        automobili_.push_back(autoPtr);   // čuva se shared_ptr, ali ne “posjeduje” u smislu ekskluzivnosti
    }

    void vozi() {
        std::cout << ime_ << " vozi automobile:\n";
        for (auto& a : automobili_) {
            a->start();
        }
    }

private:
    std::string ime_;
    std::vector<std::shared_ptr<Automobil>> automobili_; // agregacija
};

// ---- Glavni program ----
int main() {
    // Kreiranje automobila (kompozicija unutar njega drži Motor)
    auto auto1 = std::make_shared<Automobil>("BMW", 180);
    auto auto2 = std::make_shared<Automobil>("Audi", 150);

    Vozac v("Milan");

    // Agregacija: vozač koristi automobile, ali oni postoje i bez njega
    v.dodajAuto(auto1);
    v.dodajAuto(auto2);

    v.vozi();

    // Kada program završi, automobili se automatski brišu
    // Motor unutar svakog auta se takođe briše (kompozicija).
    return 0;
}
