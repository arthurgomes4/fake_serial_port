#include <iostream>
#include <unistd.h>

using namespace std;

int main(int argc, char** argv) {
    
    int counter = 0;
    while (true) {
        // print counter to console every second
        cout << "data: " << counter << endl;
        counter++;

        // delay for 1 second
        sleep(1); 
    }
}