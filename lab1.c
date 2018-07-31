/*
    This lab is all about learning to do integration using trapezoidal rule and simpson13 rule.
*/

#include <stdio.h>
#include <math.h>

#define E 2.71828
#define TRUE 1
#define FALSE 0

// definition of function1
double function1(double x){
    return 4 * pow(E, 4 * x) + 3 * pow(E, 3 * x) + 2 * pow(E, 2 * x) + pow(E, x);
}

// definition of function2
double function2(double x){
    return pow(x, 3) + 2 * x + pow(x, -1);
}

// This is a helper function used with simpson13Integration function and simply flips the isOddCoeff variable between 0 and 1. It takes in input as the pointer to that variable.
void flip(int* isOddCoeff){
    if(*isOddCoeff == 1){
        *isOddCoeff = 0;
    }
    else{
        *isOddCoeff = 1;
    }
}

// computes the integral using TRAPEZOIDAL RULE for integration. Takes in input as the function, limits and the number of segments.
double trapezoidalIntegration(double(*f)(double), double lowerLimit, double upperLimit, int numberOfSegments){
    double h = (double)(upperLimit - lowerLimit) / numberOfSegments;
    
    float value = (*f)(lowerLimit) + (*f)(upperLimit);
    for(int i = 1; i <= numberOfSegments - 1; i++){
        value += 2 * (*f)(lowerLimit + i * h);
    }
    value = value * (h / 2);
    
    return value;
}

// computes the integral using SIMPSON13 RULE for integration. Takes in input as the function, limits and the number of segments.
double simpson13Integration(double(*f)(double), double lowerLimit, double upperLimit, int numberOfSegments){
    double h = (double)(upperLimit - lowerLimit) / numberOfSegments;
    
    float value = (*f)(lowerLimit) + (*f)(upperLimit);
    int isOddCoeff = TRUE;      // this keeps track of whether we are at the odd coeff or even coeff based on whether it is TRUE OR FALSE respectively.
    int coeff;                  // changes itself to 4 or 2 based upon whether odd coeff is true or false respectively.
    for(int i = 1; i <= numberOfSegments - 1; i++, flip(&isOddCoeff)){
        coeff = isOddCoeff == TRUE ? 4 : 2;
        value += coeff * (*f)(lowerLimit + i * h);
    }
    value = value * (h / 3);
    
    return value;
}

// Driver function main
int main()
{   
    // TRAPEZOIDAL RULE for both the functions
    printf("TRAPEZOIDAL RULE / LINEAR APPROXIMATION\n");
    printf("\t-> For function1(n = 20) = %f\n", trapezoidalIntegration(function1, 1, 2, 20));
    printf("\t-> For function2(n = 20) = %f\n", trapezoidalIntegration(function2, E, 5, 20));
    
    printf("\n");
    
    // SIMPSON13 RULE for both the functions
    printf("SIMPSON13 RULE / PARABOLIC APPROXIMATION\n");
    printf("\t-> For function1(n = 20) = %f\n", simpson13Integration(function1, 1, 2, 20));
    printf("\t-> For function2(n = 20) = %f\n", simpson13Integration(function2, E, 5, 20));
    
    return 0;
}
