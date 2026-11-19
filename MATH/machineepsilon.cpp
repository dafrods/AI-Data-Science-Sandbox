#include <iostream>
#include <iomanip>
#include <cmath>

void machine_epsilon()
{
    float fEP = 1.0f, fX;
    int n = 0;
    std::cout << std::setprecision(15) << std::scientific;

    for(;;)
    {
        fX = 1.0f + fEP;
        std::cout   << std::right
                    << std::setw(20) << "fEP = " << fEP << ". n = "
                    << std::left << std::setw(20) << n << "\n";
        
        if (fX == 1.0f)
            break;

        fEP = fEP/2.0f;
        ++n;
    }

    std::cout << "\n\n Estimate of Machine Epsilon (float): " << fEP << "\n\n";

    double dEP = 1.0f, dX;
    n = 0;
    std::cout << std::setprecision(15) << std::scientific;

    for(;;)
    {
        dX = 1.0f + dEP;
        std::cout   << std::right
                    << std::setw(20) << "dEP = " << dEP << ". n = "
                    << std::left << std::setw(20) << n << "\n";
        
        if (dX == 1.0f)
            break;

        dEP = dEP/2.0f;
        ++n;
    }

    std::cout << "\n\n Estimate of Machine Epsilon (double): " << dEP << "\n\n";
}


void precision_error()
{
    int N;
    std::cout << "Input value for N: ";
    std::cin >> N;

    std::cout << std::setprecision(15) << std::scientific;

    std::cout << "Single precision results ....\n";
    const float PISP = 3.145926f;
    float fSum = 0.0f;

    for (int i = 1; i <= N; ++i)
        fSum += 1.0f/(static_cast<float>(i)*static_cast<float>(i));
    std::cout << "Forward sum is " << std::setw(20) << fSum << "\n";

    fSum =0.0f;
    for(int i = N; i >= 1; --i)
        fSum += 1.0f/(static_cast<float>(i)*static_cast<float>(i));
    std::cout << "Reverse sum is " << std::setw(20) << fSum << "\n";
    std::cout << "Exact Answer is " << PISP*PISP/6.0f << "\n\n";

//---------------------------------------------------------------------------------------

    std::cout << "Double precision results ....\n";
    const double PIDP = 3.1459265358979;
    double dSum = 0.0;

    for (int i = 1; i <= N; ++i)
        dSum += 1.0/(static_cast<float>(i)*static_cast<float>(i));
    std::cout << "Forward sum is " << std::setw(20) << dSum << "\n";

    dSum =0.0f;
    for(int i = N; i >= 1; --i)
        dSum += 1.0/(static_cast<float>(i)*static_cast<float>(i));
    std::cout << "Reverse sum is " << std::setw(20) << dSum << "\n";
    std::cout << "Exact Answer is " << PIDP*PIDP/6.0f << "\n";

}

int main()
{
    machine_epsilon();
    precision_error();
}