#ifndef _TASK_H_
#define _TASK_H_

#include <vector>
using namespace std;

class Task
{
public:
    Task(int id, int duration);
    void addDependency(Task * t);
    int computeTime();

private:
    int id;
    int duration;

    std::vector<Task*> dependencies;
};

#endif /* _TASK_H_ */
