
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

int main() {
    string line;
    int ct = 0;
    while(getline(cin, line)) {
        string left = line.substr(0, line.find(","));
        string right = line.substr(line.find(",")+1);

        int a, b, c, d;

        a = stoi(left.substr(0, left.find("-")));
        b = stoi(left.substr(left.find("-")+1));
        c = stoi(right.substr(0, right.find("-")));
        d = stoi(right.substr(right.find("-")+1));


        if(a <= c && c <= b){
            ct+=1;
        } else if (c <= a && a <= d) {
            ct+=1;
        }
    }
    cout << ct << endl;
    return 0;
}