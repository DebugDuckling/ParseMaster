// structure.h

#include <stdint.h>

typedef struct {
    char name[50];
    int8_t age;
    float height;
} Person;

typedef struct {
    char title[100];
    char author[50];
    int16_t pages;
} Book;

typedef struct {
    char make[50];
    char model[50];
    int32_t year;
} Car;

typedef struct {
    int64_t id;
    double balance;
    int8_t type;
} Account;

typedef struct {
    char code[10];
    int8_t level;
    Person manager;
    int32_t budget;
} Department;

typedef struct {
    char street[100];
    int32_t number;
    char city[50];
    char postal_code[10];
} Address;

typedef struct {
    char name[50];
    int8_t age;
    Address address;
    char position[50];
} Employee;

typedef struct {
    char name[50];
    double salary;
    int32_t department_id;
    int16_t rank;
} Position;

typedef struct {
    char id[20];
    Book favoriteBook;
    char membership_level[20];
} LibraryMember;

typedef struct {
    int64_t id;
    int32_t capacity;
    Employee employees[8];
    char industry[50];
} Company;

typedef struct {
    char name[50];
    Position positions[4];
    int8_t status;
    int16_t established_year;
} Organization;

typedef struct {
    int32_t code;
    float value;
    char unit[10];
    double threshold;
} Sensor;

typedef struct {
    char id[20];
    Account accounts[2];
    char email[50];
    char phone[15];
} User;

typedef struct {
    char name[50];
    int16_t age;
    Department departments[3];
    char location[50];
} University;

typedef struct {
    char name[50];
    int8_t rating;
    Car car;
    int32_t license_number;
} Driver;

typedef struct {
    char type[50];
    int16_t quantity;
    float price;
    char supplier[50];
} Product;

typedef struct {
    char name[50];
    double price;
    int8_t rating;
    char category[50];
} Item;

typedef struct {
    char id[20];
    Sensor sensors[6];
    char location[50];
    char status[20];
} Device;

typedef struct {
    char name[50];
    double value;
    double weight;
    char currency[10];
    char quality[20];
} Commodity;

typedef struct {
    char id[20];
    Commodity commodities[5];
    char warehouse_location[50];
    int16_t stock_level;
} Inventory;
