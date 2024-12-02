
#include <iostream> 
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

int get_prio(string s){
    char x = *s.c_str();
    if(x > 96) {
        return x - 'a' + 1;
    }
    return x - 'A' + 27;
}

int main() {
    string line;

    unordered_set<string> set;

    int prio = 0;

    vector<string> lines;

    while(getline(cin, line)) {
        lines.push_back(line);

        string l1 = line.substr(0, line.length()/2);
        unordered_set<string> set;
        for(int i = 0; i < l1.length(); i++) {
            set.insert(l1.substr(i, 1));
        }
        string l2 = line.substr(line.length()/2);
        for(int i = 0; i < l1.length(); i++) {
            if(set.find(l2.substr(i, 1)) != set.end()) {
                prio += get_prio(l2.substr(i, 1));
                break;
            }
        }
    }

    cout << "PT 1: " << prio << endl;

    int ans = 0;
    for(int i = 0; i < lines.size(); i+=3) {
        unordered_map<int, int> hm;
        for(int z = 1; z <= 97; z++){
            hm[z] = 0;
        }
        for(int j = 0; j < 3; j++) {
            string ln = lines[i+j];
            unordered_set<string> set;
            for(int k = 0; k < ln.length(); k++) {
                if(set.find(ln.substr(k, 1)) == set.end()){
                    int p = get_prio(ln.substr(k, 1));
                    hm[p]++;
                    set.insert(ln.substr(k, 1));
                }
            }
        }
        for(int z = 1; z <= 97; z++){
            if(hm[z] == 3){
                ans += z;
            }
        }
    }

    cout << "PT 2: " << ans << endl;

    return 0;
}