#include <fstream>
#include <iostream>
#include <math.h>

double p(double x, double y, double z)
{
    return z;
}

double g(double x, double y, double z)
{
    return -2*x - (pow(10, 4) + 2*exp(-x))*y - 200*cos(100*x) + exp(-x)*(pow(10,4)*cos(x) - 2*sin(100*x));
}

double k11(double x, double y, double z, double step)
{
    return step * p(x, y, z);
}

double k12(double x, double y, double z, double step)
{
    return step * g(x, y, z);
}

double k21(double x, double y, double z, double step)
{
    return step * p(x + step/2, y + k11(x,y,z,step)/2, z + k12(x,y,z,step)/2);
}

double k22(double x, double y, double z, double step)
{
    return step * g(x + step/2, y + k11(x,y,z,step)/2, z + k12(x,y,z,step)/2);
}

double k31(double x, double y, double z, double step)
{
    return step * p(x + step/2, y + k21(x,y,z,step)/2, z + k22(x,y,z,step)/2);
}

double k32(double x, double y, double z, double step)
{
    return step * g(x + step/2, y + k21(x,y,z,step)/2, z + k22(x,y,z,step)/2);
}

double k41(double x, double y, double z, double step)
{
    return step * p(x + step, y + k31(x,y,z,step), z + k32(x,y,z,step));
}

double k42(double x, double y, double z, double step)
{
    return step * g(x + step, y + k31(x,y,z,step), z + k32(x,y,z,step));
}

int main()
{
    double y0 = 1;
    double z0 = -101;
    double y1 = 1, z1 = -101;   
    double t = 0.1;
    double eps = 0.000001;
    	
    std::ofstream fout;
    fout.open("data.log"); // связываем объект с файлом
    double err;
    do 
    {
        double x = 0;
        err = 0;
        for(x; x <= 1; x += t)
        {
            z0 += (k12(x, y0, z0, t) + 2*k22(x, y0, z0, t) + 2*k32(x, y0, z0, t) + k42(x, y0, z0, t)) / 6;
            y0 += (k11(x, y0, z0, t) + 2*k21(x, y0, z0, t) + 2*k31(x, y0, z0, t) + k41(x, y0, z0, t)) / 6;

            z1 += (k12(x, y1, z1, t/2) + 2*k22(x, y1, z1, t/2) + 2*k32(x, y1, z1, t/2) + k42(x, y1, z1, t/2)) / 6;
            y1 += (k11(x, y1, z1, t/2) + 2*k21(x, y1, z1, t/2) + 2*k31(x, y1, z1, t/2) + k41(x, y1, z1, t/2)) / 6;
            z1 += (k12(x+t/2, y1, z1, t/2) + 2*k22(x+t/2, y1, z1, t/2) + 2*k32(x+t/2, y1, z1, t/2) + k42(x+t/2, y1, z1, t/2)) / 6;
            y1 += (k11(x+t/2, y1, z1, t/2) + 2*k21(x+t/2, y1, z1, t/2) + 2*k31(x+t/2, y1, z1, t/2) + k41(x+t/2, y1, z1, t/2)) / 6;
            err = (abs(y0 - y1) + abs(z0 - z1))/7;
            if (err < eps)
            {
                z1 = z0;
                y1 = y0;
            }
            else
                break;
        }
        if (x < 1)
        {
            t /= 2;
            y1 = 1;
            y0 = 1;
            z1 = -101;
            z0 = -101;
            std::cerr << "Current step: " << t << std::endl;
        }
        else
        {
            break;
        }
    } while(1);
    
    std::cout << "Step:" << t << std::endl;
    for(double x = 0, y0 = 1, z0 = -101; x <= 1; x += t)
    {
        z0 += (k12(x, y0, z0, t) + 2*k22(x, y0, z0, t) + 2*k32(x, y0, z0, t) + k42(x, y0, z0, t)) / 6;
        y0 += (k11(x, y0, z0, t) + 2*k21(x, y0, z0, t) + 2*k31(x, y0, z0, t) + k41(x, y0, z0, t)) / 6;

        fout << x << " " << y0 << std::endl;
    }
    fout.close();
}