CC     := gcc
CXX    := g++
LD     := g++
AR     := ar rc
RANLIB := ranlib

CXXFLAGS  := -Wall -fopenmp -O3
LDFLAGS   := -Wall -fopenmp -O3
LIBS      :=

OUTPUT += cpp_prueba15

all: $(OUTPUT)

SRCS += main.cpp

OBJS += $(addsuffix .o,$(basename $(SRCS)))

$(OUTPUT): $(OBJS)
	$(CXX) $(LDFLAGS) -o $@ $^ $(LIBS) 

$(OUTPUTLIB): $(OBJS)
	      $(AR) $@ $(OBJS)
	      $(RANLIB) $@

clean:
	rm $(OBJS) $(OUTPUT) *~ -rf

main.o: rectangle.h