#include <iostream>
#include <string>

using namespace std;


class Vehicle {
public:
    string brand;
    int year;
    bool isRunning;

    Vehicle(string brand, int year) {
        this->brand = brand;
        this->year = year;
        this->isRunning = false;
        cout << "Vehicle created: " << brand << " " << year << endl;
    }

    string start() {
        this->isRunning = true;
        return this->brand + " started";
    }

    string stop() {
        this->isRunning = false;
        return this->brand + " stopped";
    }

    string getInfo() {
        return this->brand + " " + to_string(this->year);
    }
};

class Car : public Vehicle {
public:
    int doors;
    int fuelLevel;

    Car(string brand, int year, int doors) : Vehicle(brand, year) {
        this->doors = doors;
        this->fuelLevel = 100;
    }

    string honk() {
        return this->brand + " honks loudly";
    }

    string refuel() {
        this->fuelLevel = 100;
        return "Car refueled";
    }

    int getDoors() {
        return this->doors;
    }
};

class Motorcycle : public Vehicle {
public:
    bool hasWindshield;

    Motorcycle(string brand, int year) : Vehicle(brand, year) {
        this->hasWindshield = false;
    }

    string rev() {
        return this->brand + " revs engine";
    }

    string wheelie() {
        return this->brand + " does a wheelie";
    }

    string addWindshield() {
        this->hasWindshield = true;
        return "Windshield added";
    }
};