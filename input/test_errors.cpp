// Test fajl sa semantičkim greškama
#include <iostream>
#include <string>

class Person {
private:
    string name;
    int age;
    
public:
    Person(string n, int a) : name(n), age(a) {}
    
    string getName() const {
        return name;
    }
    
    int getAge() const {
        return age;
    }
};

// Klasa sa greškom - nasleđuje nepostojeću klasu
class Student : public NonExistentClass {
private:
    string studentId;
    
public:
    Student(string n, int a, string id) : Person(n, a), studentId(id) {}
    
    string getStudentId() const {
        return studentId;
    }
};

// Klasa sa duplikat članom
class Teacher {
private:
    string name;  // Duplikat - već postoji u Person
    string department;
    
public:
    Teacher(string n, string dept) : name(n), department(dept) {}
    
    string getDepartment() const {
        return department;
    }
};
