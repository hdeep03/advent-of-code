
#include <iostream> 
#include <string>
#include <vector>
using namespace std;


int main() {
    string line;
    vector<int> v;
    v.push_back(0);

    while(getline(cin, line)) {
        if(line.length() == 0) {
            v.push_back(0);
        } else {
            v[v.size()-1] += stoi(line);
        }
    }

    sort(v.begin(), v.end(), greater<int>());

    cout << "PT1: " << v[0] << endl;
    int sum = 0;
    for(int i = 0; i < 3; i++){
        sum += v[i];
    }
    cout << "PT2: " << sum << endl;

    return 0;
}