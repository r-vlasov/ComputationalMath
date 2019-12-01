#!/usr/bin/gnuplot -persist

set terminal png enhanced
set output "plot.png"

set size ratio 0.5
set autoscale y
set grid
set title "Runge-Kutta 4th"
plot "data.log" using 1:2 notitle with linespoints lt rgb '#FF0000' lw 2 pt 7 ps 1;