#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <boost/lexical_cast.hpp>
#include <boost/tokenizer.hpp>
#include <boost/foreach.hpp>
#include <boost/unordered_map.hpp>

using namespace std;

#include "Task.h"

std::vector<int> splitString(string str){

    boost::char_separator<char> sep(", ");
    
    boost::tokenizer<boost::char_separator<char> > tokens(str, sep);
    std::vector<int> returnVect;
    BOOST_FOREACH(string t, tokens){
        returnVect.push_back(boost::lexical_cast<int>(t));
    }

    return returnVect;
}


int main(int argc, char *argv[])
{
    ifstream tasksFile;
    tasksFile.open("in");
    if(tasksFile.fail()){
        cout << "ERROR al abrir el fichero" << endl;
        return -1;
    }

    string currentLine;

    int fileSection = 0;
    int taskId;

    boost::unordered_map<int, Task*> tasksMap;

    while(!tasksFile.eof()){
        getline(tasksFile, currentLine);

        if (currentLine[0] == '#'){
            fileSection += 1;
        }else if (currentLine == ""){
            continue;
        }else{
            std::vector<int> components = splitString(currentLine);

            if (fileSection == 1){
                // who minds
            }else if(fileSection == 2){
                if(components.size() != 2){
                    cout << "ERROR @ '" << currentLine << "'" << endl;
                    return -1;
                }

                tasksMap[components[0]] = new Task(components[0], components[1]);
            }else{
                if(components.size() < 2){
                    cout << "ERROR @ " << currentLine << endl;
                    return -1;
                }

                taskId = components[0];
                
                for (unsigned i = 1; i < components.size(); ++i){
                    tasksMap[taskId] -> addDependency(tasksMap[components[i]]);
                    
                }
            }
        }        
    }

    tasksFile.close();
    getline(cin, currentLine);
    std::vector<int> tasksToCheck = splitString(currentLine);

    BOOST_FOREACH (int i, tasksToCheck)
    {
        cout << i << " " << tasksMap[i] -> computeTime() << endl;
    }

    for(boost::unordered_map<int, Task*>::iterator i = tasksMap.begin(); i != tasksMap.end(); ++i){
        delete i -> second;
    }

    return 0;
}
