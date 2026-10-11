.PHONY: run clean python c sh

CC = gcc
CFLAGS = -Wall -Werror -Wextra -pedantic
JAVAC = javac
JAVA = java

python:
	./Solution.py

java:
	$(JAVAC) ./Solution.java && $(JAVA) Solution

c:
	$(CC) -o solution $(CFLAGS) Solution.c -lm && ./solution

sh:
	./Solution.sh

clean:
	rm *.class solution
