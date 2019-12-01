#!/bin/bash

g++ task.cpp -o 7.exe
./7.exe
set output "plot.png"

set size ratio 0.01
gnuplot plot.sh
feh plot.png