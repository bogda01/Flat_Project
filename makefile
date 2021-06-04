all : Source
	cp ./Source ../Source
	
Source : Source.o
	g++ ./Source.o -o ./Source -I/usr/local/lib -lsfml-graphics -lsfml-window -lsfml-system
	
Source.o : Source.cpp
	g++ -c ./Source.cpp -I/usr/local/include 

clean :
