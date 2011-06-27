#ifndef _RECTANGLE_H_
#define _RECTANGLE_H_

#include <utility>
using namespace std;

class Rectangle
{
public:
    int x1, y1, x2, y2;
    int color;
    int area;

    Rectangle(int x1, int y1, int x2, int y2, int color) 
        : x1(x1), y1(y1), x2(x2), y2(y2), color(color){
        
        if (x2 - x1 <= 0 || y2 - y1 <= 0){
            area = 0;
        }else{
            area = (x2 - x1) * (y2 - y1);
        }
    }

    std::pair<int,int> checkRow(int row){
        if (row >= y1 && row < y2){
            return make_pair(x1, x2 - 1);
        }else{
            return make_pair(-1, -1);
        }
    }
};

#endif /* _RECTANGLE_H_ */
