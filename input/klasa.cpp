#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Bazna klasa
class Osoba {
protected:
    string ime;
    int godine;
public:
    Osoba(const string& i, int g) {
        ime = i;
        godine = g;
    }
    void predstaviSe() {
        cout << "Ja sam " << ime << ", imam " << godine << " godina." << endl;
    }
    string getIme() {
        return ime;
    }
    ~Osoba() {}
};

// Izvedena klasa Student
class Student : public Osoba {
private:
    string indeks;
    vector<string> predmeti;
public:
    Student(const string& i, int g, const string& ind) : Osoba(i, g) {
        indeks = ind;
    }

    void dodajPredmet(const string& predmet) {
        predmeti.push_back(predmet);
    }

    void predstaviSeStudent() {
        cout << "Student " << ime << " (" << indeks << "), godina: " << godine << endl;
        cout << "Predmeti: ";
        for (int i = 0; i < predmeti.size(); i++)
            cout << predmeti[i] << " ";
        cout << endl;
    }
};

// Izvedena klasa Profesor
class Profesor : public Osoba {
private:
    string katedra;
    vector<Student*> studenti;
public:
    Profesor(const string& i, int g, const string& k) : Osoba(i, g) {
        katedra = k;
    }

    void dodajStudenta(Student* s) {
        studenti.push_back(s);
    }

    void predstaviSeProfesor() {
        cout << "Profesor " << ime << ", katedra: " << katedra << ", godina: " << godine << endl;
        cout << "Studenti na katedri: ";
        for (int i = 0; i < studenti.size(); i++)
            cout << studenti[i]->getIme() << " ";
        cout << endl;
    }
};

// Klasa Kurs
class Kurs {
private:
    string naziv;
    Profesor* predavac;
    vector<Student*> polaznici;
public:
    Kurs(const string& n, Profesor* p) {
        naziv = n;
        predavac = p;
    }

    void upisiStudenta(Student* s) {
        polaznici.push_back(s);
        predavac->dodajStudenta(s);
    }

    void ispisiPolaznike() {
        cout << "Kurs: " << naziv << endl;
        cout << "Predavac: " << predavac->getIme() << endl;
        cout << "Polaznici: ";
        for (int i = 0; i < polaznici.size(); i++)
            cout << polaznici[i]->getIme() << " ";
        cout << endl;
    }
};

int main() {
    Student* s1 = new Student("Mila", 22, "RA123");
    Student* s2 = new Student("Ana", 21, "RA124");

    Profesor* p1 = new Profesor("Marko", 45, "Matematika");

    Kurs* k1 = new Kurs("Algebra", p1);
    k1->upisiStudenta(s1);
    k1->upisiStudenta(s2);

    s1->dodajPredmet("Algebra");
    s2->dodajPredmet("Algebra");

    s1->predstaviSeStudent();
    s2->predstaviSeStudent();
    p1->predstaviSeProfesor();
    k1->ispisiPolaznike();

    delete s1;
    delete s2;
    delete p1;
    delete k1;

    return 0;
}
