
#include <iostream> 
#include <sstream> 
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;


int main() {
    string line;
    cin >> line;
    for(int i = 0; i < line.length()-3; i++) {
        unordered_set<int> set;
        bool clear = true;
        for(int j = 0; j < 4; j++){
            if(set.find(line[i+j]) != set.end()){
                clear = false;
                break;
            }
            set.insert(line[i+j]);
        }
        if(clear){
            cout << i+4 << endl;
            break;
        }
    }
    for(int i = 0; i < line.length()-13; i++) {
        unordered_set<int> set;
        bool clear = true;
        for(int j = 0; j < 14; j++){
            if(set.find(line[i+j]) != set.end()){
                clear = false;
                break;
            }
            set.insert(line[i+j]);
        }
        if(clear){
            cout << i+14 << endl;
            return 0;
        }
    }
    return 0;
}