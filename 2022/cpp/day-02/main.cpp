#include <string>
#include <vector>
#include <iostream>
using namespace std;

int p_state(int as, string oc) {
    switch ((int)(*oc.c_str() - 'X')) {
        case 0: {
            return (as + 2) % 3;
        } case 1: {
            return as;
        } case 2: {
            return (as + 1)%3;
        }
    }
}

int a_state(string s) {
    return (int)(*s.c_str() - 'A');
}

int get_points(int a, int b){
    int score = b + 1;
    if (b == (a + 1)%3){
        score += 6;
    } else if (a==b) {
        score += 3;
    }
    return score;
}

int main() {

    string line;
    int sum = 0;
    while(getline(cin, line)) {
        int a_s = a_state(line.substr(0, 1));
        sum += get_points(a_s, p_state(a_s, line.substr(2, 3)));
    }
    cout << sum << endl;
}