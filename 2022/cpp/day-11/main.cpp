
#include <iostream> 
#include <sstream> 
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define ll long long

struct monkey {
    vector<ll> items;
    int test;
    int t;
    int f;
    function<ll(ll)> func;
};

int main() {

    auto file = ifstream("inputs/11.in");
    cin.rdbuf(file.rdbuf());

    vector<string> lines;
    string line;
    while(getline(cin, line)) {
        lines.push_back(line);
    }

    int n = (lines.size()+1)/7;
    vector<monkey> monkeys;
    for(int i = 0; i < n; i++) {
        monkey m;
        m.items = vector<ll>();
        string ln = lines[i*7 + 1].substr(18);
        while(ln.find(",") != string::npos) {
            m.items.push_back(stoi(ln.substr(0, ln.find(","))));
            ln = ln.substr(ln.find(",") + 1);
        }
        m.items.push_back(stoi(ln));
        bool add = lines[i*7 + 2][23] == '+';
        m.test = stoi(lines[i*7 + 3].substr(20));
        m.t = stoi(lines[i*7 + 4].substr(28));
        m.f = stoi(lines[i*7 + 5].substr(29));

        int operand = 0;
        // cout << lines[i*7 + 2].substr(24) << endl;
        if(lines[i*7 + 2].substr(24).find("old") != string::npos) {
            operand = 0;
        } else {
            operand = stoi(lines[i*7 + 2].substr(24));
        }
        if(add) {
            m.func = [operand](ll x) {
                return x + operand;
            };
        } else if (operand != 0){
            m.func = [operand](ll x) {
                return x * operand;
            };
        } else {
            m.func = [&](ll x) {
                return x*x;
            };
        }
        monkeys.push_back(m);
    }

    vector<int> inspects;
    for(int i = 0; i < monkeys.size();i++){
        inspects.push_back(0);
    }    

    int factor = 1;
    for(monkey m: monkeys) {
        factor *= m.test;
    }

    for(int r = 1; r <= 10000; r++) {
        for(int k = 0; k < n; k++) {
            monkey& m = monkeys[k];
            for(int i = 0; i < m.items.size(); i++) {
                m.items[i] = m.func(m.items[i]%factor)%factor;
            }
            inspects[k] = inspects[k] + m.items.size();
            vector<ll> items;
            vector<int> dest;
            for(int i = 0; i < m.items.size(); i++) {
                if(m.items[i] % m.test == 0) {
                    dest.push_back(m.t);
                } else {
                    dest.push_back(m.f);
                }
                items.push_back(m.items[i]);
            }
            monkeys[k].items.clear();
            for(int i = 0; i < items.size(); i++) {
                monkeys[dest[i]].items.push_back(items[i]);
            }
        }
    }
    sort(inspects.begin(), inspects.end(), greater<int>());
    cout << ((long long)inspects[0]) * ((long long)inspects[1]) << endl;
    return 0;
}