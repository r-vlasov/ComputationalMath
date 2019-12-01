#include <fstream>
#include <iostream>
#include <math.h>

double f(double x)
{
    return exp(-2*x)* pow((cos(x) - sin(x))/cos(x), 2);
}

double k1(double x)
{
    return f(x);
}

double k2(double x, double t)
{
    return f(x + t/2);
}

double k3(double x, double t)
{
    return f(x+t);
}


int main()
{
    double y0 = 0;
    double y1 = 0;   
    double t = 0.1;
    double eps = 0.000001;
    	
    std::ofstream fout;
    fout.open("data.log"); // связываем объект с файлом
    double err = 0;
    do 
    {
        err = 0;
        double x = 0;
        for(x; x <= 1; x += t)
        {
            y0 += t*(k1(x) + 4*k2(x, t) + k3(x, t))/6;
            y1 += t/2 * (k1(x) + 4*k2(x, t/2) + k3(x, t/2))/6;
            y1 += t/2 * (k1(x+t/2) + 4*k2(x+t/2, t/2) + k3(x+t/2, t/2))/6;
            err += abs(y0 - y1);
        }
        if (err <= eps)
        {
            break;
        }
        else
        {
            t /= 2;
            y1 = 0;
            y0 = 0;
        }
        
    } while(1);
    
    std::cout << "Step:" << t << std::endl;
    std::cout << "Global error = " << err;
    for(double x = 0, y0=0; x <= 1; x += t)
    {
        y0 += t*(k1(x) + 4*k2(x, t) + k3(x, t))/6;
        fout << x << " " << y0 << std::endl;
    }
    fout.close();
}