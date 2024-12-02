
#include <iostream> 
#include <sstream> 
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;


int main() {
    string line;
    vector<string> lines;

    int max_stack = 0;
    bool set = false;

    while(getline(cin, line)) {
        lines.push_back(line);
        if(!set){
            try {
                stoi(line);
                set = true;
            } catch (exception e) {
                max_stack++;
            }
        }
    }

    vector<vector<int>> stacks;
    int num_stacks = (lines[max_stack].length()+1)/4;
    for(int i = 0; i < num_stacks; i++){
        vector<int> stack;
        stacks.push_back(stack);
    }

    for(int i = max_stack - 1; i >= 0; i--)
    {
        for(int j = 1; j < lines[i].length(); j+= 4) {
            if(65 <= lines[i][j]  && lines[i][j] <= 90) {
                stacks[(j-1)/4].push_back(lines[i][j]);
            }
        }
    }


    for(int i = max_stack + 2; i < lines.size(); i++) {
        int a = stoi(lines[i].substr(lines[i].find("move")+4));\
        int b = stoi(lines[i].substr(lines[i].find("from")+4));
        int c = stoi(lines[i].substr(lines[i].find("to")+2));

        vector<int> temp;

        for(int z = 0; z < a; z++) {
            temp.push_back(stacks[b-1][stacks[b-1].size()-1]);
            stacks[b-1].pop_back();
        }
        for(int z = 0; z<a;z++){
            stacks[c-1].push_back(temp[a-z-1]);
        }
    }
    for(int i = 0; i < stacks.size(); i++) {
        cout << (char)stacks[i].back();
    }
    cout << endl;

    return 0;
}