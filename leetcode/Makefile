.PHONY: run clean python c sh cpp java

CC = gcc
CPP = g++
CFLAGS = -Wall -Werror -Wextra -pedantic
CPPFLAGS =
JAVAC = javac
JAVA = java

python:
	./Solution.py

java:
	$(JAVAC) ./Solution.java && $(JAVA) Solution

c:
	$(CC) -o solution $(CFLAGS) Solution.c -lm && ./solution

cpp:
	$(CPP) -o solution $(CPPFLAGS) Solution.cpp && ./solution

sh:
	./Solution.sh

clean:
	rm *.class solution
