#include<String>
using namespace std;
class Person {
private:
    std::string name;
    int age;
    
public:
    Person(const std::string& n, int a);
    std::string getName() const;
    int getAge() const;
    void setName(const std::string& n);
    void setAge(int a);
    virtual void display() const;
    virtual ~Person();
};

class Student : public Person {
private:
    std::string studentId;
    double gpa;
    
public:
    Student(const std::string& n, int a, const std::string& id, double g);
    std::string getStudentId() const;
    double getGpa() const;
    void setGpa(double g);
    void display() const override;
};
