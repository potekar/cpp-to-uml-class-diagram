// Simple C++ example with basic class structure
#include <iostream>
#include <string>
using namespace std;
class Person {
private:
    string name;
    int age;
    
public:
    Person(const string& n, int a) : name(n), age(a) {}
    
    string getName() const {
        return name;
    }
    
    int getAge() const {
        return age;
    }
    
    void setName(const string& n) {
        name = n;
    }
    
    void setAge(int a) {
        age = a;
    }
    
    virtual void display() const {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
    
    virtual ~Person() = default;
};

class Student : public Person {
private:
    string studentId;
    double gpa;
    
public:
    Student(const string& n, int a, const string& id, double g) 
        : Person(n, a), studentId(id), gpa(g) {}
    
    string getStudentId() const {
        return studentId;
    }
    
    double getGpa() const {
        return gpa;
    }
    
    void setGpa(double g) {
        gpa = g;
    }
    
    void display() const override {
        Person::display();
        cout << "Student ID: " << studentId << ", GPA: " << gpa << endl;
    }
};

class Teacher : public Person {
private:
    string department;
    int yearsOfExperience;
    
public:
    Teacher(const string& n, int a, const string& dept, int years) 
        : Person(n, a), department(dept), yearsOfExperience(years) {}
    
    string getDepartment() const {
        return department;
    }
    
    int getYearsOfExperience() const {
        return yearsOfExperience;
    }
    
    void display() const override {
        Person::display();
        cout << "Department: " << department << ", Experience: " << yearsOfExperience << " years" << endl;
    }
};
