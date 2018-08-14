// LAB - 2: PILLAR DESIGN IN BOARD AND PILLAR METHOD USING THE TRIBUTARY AREA METHOD
// Submitted by - Suresh Gandhi 14MI31024

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Declaration of the base function used.
float baseFunction(float A1, float A2, float A3, float A4, float wp) {
	return A1 * pow(wp, 3) + A2 * pow(wp, 2) + A3 * pow(wp, 1) + A4;
}

// Declaration of the derivative of the base function used.
float baseFunctionDerivative(float A1, float A2, float A3, float wp) {
	return 3 * A1*pow(wp, 2) + 2 * A2*pow(wp, 1) + A3;
}

// A helper function which is used to calculate the slope.
float calculateSlope(double x[], double y[], int n) {
	// Declaring the used variables beforehand.
	float sum_x, sum_y, sum_xy, sum_x2;

	sum_x = 0;
	for (int i = 0; i<n; i++) {
		sum_x = sum_x + x[i];
	}

	sum_y = 0;
	for (int i = 0; i<n; i++) {
		sum_y = sum_y + y[i];
	}

	sum_xy = 0;
	for (int i = 0; i<n; i++) {
		sum_xy = sum_xy + x[i] * y[i];
	}

	sum_x2 = 0;
	for (int i = 0; i<n; i++) {
		sum_x2 = sum_x2 + x[i] * x[i];
	}

	return (n*sum_xy - sum_x * sum_y) / (n*sum_x2 - sum_x * sum_x);
}

// A helper function which is used to calculate the intercept.
float calculateIntercept(double x[], double y[], int n){
	// Declaring the used variables beforehand.
	float sum_x, sum_y, sum_xy, sum_x2;

	sum_x = 0;
	for(int i=0; i<n; i++){
		sum_x = sum_x + x[i];
	}

	sum_y = 0;
	for(int i=0; i<n; i++){
		sum_y = sum_y + y[i];
	}

	sum_xy = 0;
	for(int i=0; i<n; i++){
		sum_xy = sum_xy + x[i]*y[i];
	}

	sum_x2 = 0;
	for(int i=0; i<n; i++){
		sum_x2 = sum_x2 + x[i]*x[i];
	}
	
	return (sum_y*sum_x2 - sum_x*sum_xy)/(n*sum_x2 - sum_x*sum_x);
}


int main(){
	// Prompts the user to enter the number of observations.
	cout << "USER INPUT: NO OF OBSERVATIONS " << endl;
	
	// Declaring the size and the strength arrays of size 100 presently.
	double  size[100], strength[100];
	int n;
	cin >> n;
	
	// Prompts the user to enter the size array elements one by one.
	cout << "USER INPUT: ENTER SIZE ARRAY ONE BY ONE " << endl;
	for(int i=0; i<n; i++){
		cin >> size[i];
		size[i] = log(size[i]);
	}

	// Prompts the user to enter the strength array elements one by one.
	cout << "USER INPUT: ENTER STRENGTH ARRAY ONE BY ONE " << endl;
	for(int i=0; i<n; i++){
		cin >> strength[i]; 
		strength[i] = log(strength[i]);
	}
	
	// Prompts the user to enter the other used parameters.
	float pillarHeight, galleryWidth, row, H, factorOfSafety, g;
	cout << "USER INPUT: HEIGHT OF THE PILLAR" << endl;
	cin >> pillarHeight;
	cout << "USER INPUT: WIDTH OF THE GALLERY" << endl;
	cin >> galleryWidth;
	cout << "USER INPUT: ROW" << endl;
	cin >> row;
	cout << "USER INPUT: DEPTH" << endl;
	cin >> H;
	cout << "USER INPUT: FOS" << endl;
	cin >> factorOfSafety;
	cout << "USER INPUT: GRAVITATION" << endl;
	cin >> g;
	
	// Doing calculations.
	float S_1 = 1000*exp(calculateIntercept(size, strength,n))*pow(1000,calculateSlope(size, strength,n));
	cout << "USER OUTPUT: Value of S1(KPa units) = " << S_1 << endl;
	
	float A1 = 0.36*S_1/pillarHeight ;
	float A2 = 0.64*S_1 - H*row*g*factorOfSafety;
	float A3 = -2*row*g*H*factorOfSafety*galleryWidth;
	float A4 = -1*row*g*H*factorOfSafety*galleryWidth*galleryWidth;
	
	cout << "A1 = " << A1 << endl;
	cout << "A2 = " << A2 << endl;
	cout << "A3 = " << A3 << endl;
	cout << "A4 = " << A4 << endl;
	
	float w1 = 1000, w0;
	
	do
	{
		w0 = w1;
		w1 = w0 - baseFunction(A1,A2,A3,A4,w0)/baseFunctionDerivative(A1,A2,A3,w0) ;
//		cout << w1 << "    " ;
	}while(fabs(w1-w0)>=0.01);
	
	cout << "USER OUTPUT: Width of the pillar(metres) is -> " << w1;
	
	return 0;
}
