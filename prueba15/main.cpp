#include <iostream>
#include <string>
#include <utility>

using namespace std;

#include "rectangle.h"

#include <boost/lexical_cast.hpp>
#include <boost/tokenizer.hpp>
#include <boost/foreach.hpp>
#include <boost/unordered_map.hpp>
#include <map>

#include <omp.h>


std::vector<int> splitString(string str){

    boost::char_separator<char> sep(", ");
    
    boost::tokenizer<boost::char_separator<char> > tokens(str, sep);
    std::vector<int> returnVect;
    BOOST_FOREACH(string t, tokens){
        returnVect.push_back(boost::lexical_cast<int>(t));
    }

    return returnVect;
}

void reset (int * row, int items, int value = 1){
    for (int i = 0; i < items; ++i){
        row[i] = value;
    }
}

void pRow(int * row, int N){
    for (int i = 0; i < N; ++i)
    {
        cout << row[i] << " ";
    }
    cout << endl;
}

int main(int argc, char *argv[])
{
    string currentLine;

    int numProcessors = 8;
    omp_set_num_threads(numProcessors);

    while(getline(cin, currentLine)){
        std::vector<int> lineElements = splitString (currentLine);

        unsigned canvasWidth = lineElements[0];
        unsigned canvasHeight = lineElements[1];
        unsigned numRectangles = lineElements[2];

        Rectangle ** rectangleList = new Rectangle*[numRectangles];

        int maxColor = 0;

        // Reading rectangles from stdin
        for (unsigned i = 0; i < numRectangles; ++i){
            int x1 = lineElements[3 + i * 5];
            int y1 = lineElements[4 + i * 5];
            int x2 = lineElements[5 + i * 5];
            int y2 = lineElements[6 + i * 5];
            int color = lineElements[7 + i*5];

            if (color > maxColor)
                maxColor = color;
         
            rectangleList[i] = new Rectangle(x1, y1, x2, y2, color);
        }

        int * foundColors = new int[maxColor + 1];
        reset(foundColors, maxColor + 1, 0);

#pragma omp parallel
        {
            
            int processorId = omp_get_thread_num();

            int * currentRow = new int[canvasWidth];

            pair<int,int> thisPair;

            int * foundColorsLocal = new int[maxColor + 1];
            reset(foundColorsLocal, maxColor + 1, 0);

            for (unsigned i = processorId; i < canvasHeight; i += numProcessors){
                reset(currentRow, canvasWidth);

                for (unsigned j = 0; j < numRectangles; ++j){
                    thisPair = rectangleList[j] -> checkRow(i);

                    if (thisPair.first != -1){
                        for (int k = thisPair.first; k <= thisPair.second; ++k){
                            currentRow[k] = rectangleList[j] -> color;
                        }
                    }//*/
                }

                for(unsigned j = 0; j < canvasWidth; ++j){
                    foundColorsLocal[currentRow[j]] += 1;
                }         
            }

#pragma omp critical
            {
                for(int i = 0; i < maxColor + 1; ++i){
                    foundColors[i] += foundColorsLocal[i];
                }
            }
            

            delete[] currentRow;
            delete[] foundColorsLocal;

        } // fin omp parallel
        
        std::vector<pair<int,int> > finalColors;

        for (int i = 0; i < maxColor + 1; ++i){
            if(foundColors[i] != 0){                
                finalColors.push_back(make_pair(i, foundColors[i]));
            }
        }

        
        unsigned i;
        for (i = 0; i < finalColors.size() - 1; ++i){
            cout << finalColors[i].first << " " << finalColors[i].second << " ";
        }
        cout << finalColors[i].first << " " << finalColors[i].second << endl;
        //*/
        
        // DESTRUCTORS 
        delete[] foundColors;
        for (unsigned i = 0; i < numRectangles; ++i){
            delete rectangleList[i];
        }
        delete[] rectangleList;
    }

    return 0;
}
