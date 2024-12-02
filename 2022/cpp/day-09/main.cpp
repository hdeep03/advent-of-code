
#include <iostream> 
#include <sstream> 
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <unordered_set>
#include <unordered_map>

using namespace std;

struct point {
    int x;
    int y;
};

void update_tail(point &head, point &tail) {
    bool found = false;
    for(int i = -1; i <= 1; i++){
        for(int j = -1; j<=1;j++){
            if(head.x + i == tail.x && head.y + j == tail.y) {
                found = true;
            }
        }
    }
    if(found){
        return;
    }
    int min_dist = 1000000;
    int min_x = 0;
    int min_y = 0;
    for(int i = -1; i <= 1; i++){
        for(int j = -1; j<=1;j++){
            int dist = pow(head.x - tail.x - i, 2) + pow(head.y - tail.y - j, 2);
            if(dist < min_dist) {
                min_dist = dist;
                min_x = i;
                min_y = j;
            }
        }
    }
    tail.x += min_x;
    tail.y += min_y;
}

int hash_point(point p) {
    return p.x * 1000 + p.y;
}

int main() {
    string line;
    vector<point> points;
    for(int i = 0; i < 10; i++){
        points.push_back({0, 0});
    }

    unordered_set<int> visited;
    
    while(getline(cin, line)) {
        char dir = line[0];
        vector<int> offset = {0, 0};
        switch(dir){
            case 'R':
                offset = {1, 0};
                break;
            case 'L':
                offset = {-1, 0};
                break;
            case 'U':
                offset = {0, 1};
                break;
            case 'D':
                offset = {0, -1};
                break;
        }
        for(int i = 0; i < stoi(line.substr(1)); i++) {
            points[0].x += offset[0];
            points[0].y += offset[1];
            for(int i = 1; i < points.size(); i++){
                update_tail(points[i-1], points[i]);
            }
            visited.insert(hash_point(points.back()));
        }
    }
    cout << visited.size() << endl;
    
    return 0;
}