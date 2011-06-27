CC     := gcc
CXX    := g++
LD     := g++
AR     := ar rc
RANLIB := ranlib

CXXFLAGS  := -Wall -g
LDFLAGS   := -Wall -g
LIBS      :=

OUTPUT += 4_tasks

all: $(OUTPUT)

SRCS += Task.cpp main.cpp

OBJS += $(addsuffix .o,$(basename $(SRCS)))

$(OUTPUT): $(OBJS)
	$(CXX) $(LDFLAGS) -o $@ $^ $(LIBS) 

$(OUTPUTLIB): $(OBJS)
	      $(AR) $@ $(OBJS)
	      $(RANLIB) $@

clean:
	rm $(OBJS) $(OUTPUT) *~ -rf

Task.o: Task.h
main.o: Task.h
