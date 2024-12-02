
#include <iostream> 
#include <sstream> 
#include <fstream>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;


unordered_set<int> get_indicies(vector<vector<int>> matrix, int t_x, int t_y, vector<vector<int>> starts, int n, int m){
    unordered_set<int> top;
    for(vector<int> start: starts) {
        int max_val = -1;
        int x = start[0];
        int y = start[1];
        while (0 <= x && x < matrix.size() && 0 <= y && y < matrix[0].size()) {
            if(matrix[x][y] > max_val) {
                max_val = matrix[x][y];
                top.insert(x*m + y);
            }
            x += t_x;
            y += t_y;
        }
    }
    return top;

}

int get_scenic_score(vector<vector<int>> matrix, int i, int j, int n, int m) {
    int score = 1;
    int height = matrix[i][j];
    vector<vector<int>> offsets = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    for(vector<int> offset: offsets) {
        int x = i + offset[0];
        int y = j + offset[1];
        int ct = 0;
        while(0 <= x && x < n && 0 <= y && y < m) {
            ct++;
            if(matrix[x][y] >= height) {
                break;
            }
            x += offset[0];
            y += offset[1];
        }
        score *= ct;
    }
    return score;
}

int main() {
    ifstream file("inputs/8.in");
    cin.rdbuf(file.rdbuf());

    vector<vector<int>> matrix;
    string line;
    int i = 0;
    int n = 0, m = 0;
    while(getline(cin, line)) {
        matrix.push_back(vector<int>());
        for(int j = 0; j < line.size(); j++) {
            matrix[i].push_back(line[j]);
        }
        i++;
        m = line.size();
    }
    n = matrix.size();
    // Do left to right pass
    vector<vector<int>> starts;
    for(int i = 0; i < matrix.size(); i++) {
        starts.push_back({i, 0});
    }
    unordered_set<int> left = get_indicies(matrix, 0, 1, starts, n, m);

    // Do right to left pass
    starts.clear();
    for(int i = 0; i < matrix.size(); i++) {
        starts.push_back({i, m - 1});
    }
    unordered_set<int> right = get_indicies(matrix, 0, -1, starts, n, m);

    // Do top to bottom pass
    starts.clear();
    for(int i = 0; i < matrix[0].size(); i++) {
        starts.push_back({0, i});
    }
    unordered_set<int> top = get_indicies(matrix, 1, 0, starts, n, m);

    // Do bottom to top pass
    starts.clear();
    for(int i = 0; i < matrix[0].size(); i++) {
        starts.push_back({n - 1, i});
    }
    unordered_set<int> bottom = get_indicies(matrix, -1, 0, starts, n, m);

    unordered_set<int> result;

    for(int i: left) {
        result.insert(i);
    }
    for(int i: right) {
        result.insert(i);
    }
    for(int i: top) {
        result.insert(i);
    }
    for(int i: bottom) {
        result.insert(i);
    }
    cout << "PT1: " << result.size() << endl;

    int max_scc = -1;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            int scc = get_scenic_score(matrix, i, j, n, m);
            cout << i << " " << j << " " << scc << endl;
            if(scc > max_scc) {
                max_scc = scc;
            }
        }
    }
    cout << "PT2: " << max_scc << endl;

}