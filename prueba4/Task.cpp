#include "Task.h"

Task::Task(int id, int duration) : id(id), duration(duration){ }

void Task::addDependency(Task * t){
    dependencies.push_back(t);
}

int Task::computeTime(){
    if(dependencies.empty()){
        return duration;
    }else{
        int maxDuration = 0;
        for(std::vector<Task *>::const_iterator i = dependencies.begin(); i != dependencies.end(); ++i){
            int thisDependencyDuration = (*i) -> computeTime();
            if(thisDependencyDuration > maxDuration){
                maxDuration = thisDependencyDuration;
            }
        }

        return duration + maxDuration;
    }
}
