
#include <iostream> 
#include <sstream> 
#include <fstream>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

string is_lit(int x, int cycle) {
    if (abs(cycle%40-x) <= 1) {
        return "#";
    } else {
        return ".";
    }

}

int main() {
    string line;
    int cycle = -1;

    int x = 1;
    string res = "";

    while(getline(cin, line)) {
        if(line.length() == 4) {
            cycle++;
            res += is_lit(x, cycle);

        } else {
            int dx = stoi(line.substr(4, line.length() - 4));
            cycle++;
            res += is_lit(x, cycle);
            cycle++;
            res += is_lit(x, cycle);
            x += dx;
        }
    }
    cout << cycle << endl;
    for(int i = 0; i < 6; i++){
        cout << res.substr(i*40, 40) << endl;
    }
    return 0;
}