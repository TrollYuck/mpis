#include <iostream>
#include <iostream>
#include <fstream>
#include <array>
#include <random>
#include <vector>
#include <string>
#include <time.h>
#define _USE_MATH_DEFINES
#include <math.h>

static std::random_device rd;
static std::mt19937 mt(rd());
static std::ofstream file("monte_carlo.txt");


std::array<double, 2> rand_point(double a, double b, double M) {
	std::uniform_real_distribution<double> w{ a, b };
	std::uniform_real_distribution<double> h{ 0, M };
	std::array<double, 2> point{};
	double x = 0;
	x = w(mt);
	double y = 0;
	y = h(mt);
	point[0] = x;
	point[1] = y;
	return point;
}

std::vector<double> init_n_array() {
	double n = 50.0;
	std::vector<double> n_array;
	do {
		n_array.push_back(n);
		n += 50;
	} while (n <= 5000);
	return n_array;
}

double f_1(double x) {
	return pow(x, 1.0 / 3.0); //M = 2, a = 0, b = 8, diff = 12
}

double f_2(double x) {
	return sin(x); //M = 1, a = 0, b = pi, diff = 2
}


double f_3(double x) { //M = 27/64 = 0.421875, a = 0, b = 1, diff = 0.2
	double y = 1.0 - x;
	y = pow(y, 3.0);
	y *= 4.0 * x;
	return y;
}

double pi_(double x) { //M = 1, a = 0, b = 1, diff = pi/4 ~ 0.785398
	return pow((1 - pow(x, 2.0)), 1.0 / 2.0);
}

enum Functions
{
	f1, f2, f3, pi
};

int count_C(Functions choice, double n, double a, double b, double M) {
	int C = 0;
	switch (choice)
	{
	case f1:
		for (int i = 0; i < n; i++){
			std::array<double, 2> point = rand_point(a, b, M);
			double test = f_1(point[0]);
			if (point[1] <= test )
				C++;
		}
		break;
	case f2:
		for (int i = 0; i < n; i++) {
			std::array<double, 2> point = rand_point(a, b, M);
			if (point[1] <= f_2(point[0]))
				C++;
		}
		break;
	case f3: 
		for (int i = 0; i < n; i++) {
			std::array<double, 2> point = rand_point(a, b, M);
			if (point[1] <= f_3(point[0]))
				C++;
		}
		break;
	case pi:
		for (int i = 0; i < n; i++) {
			std::array<double, 2> point = rand_point(a, b, M);
			if (point[1] <= pi_(point[0]))
				C++;
		}
		break;
	default:
		break;
	}
	return C;
}

double approx(Functions choice, double n, double a, double b, double M) {
	double integral = 0;
	integral = count_C(choice, n, a, b, M);
	integral /= n;
	integral *= (b - a) * M;
	return integral;
}

std::vector<std::array<double, 2>> simulate(Functions choice, int k, double a, double b, double M) {
	std::vector<std::array<double, 2>> c_n;
	std::vector<double> n_array = init_n_array();
	for (int n : n_array) {
		for (int i = 0; i < k; i++) {
			double integral_approx = approx(choice, n, a, b, M);
			std::array<double, 2> point{(double)integral_approx, n};
			c_n.push_back(point);
			file << integral_approx << " " << n << std::endl;
			std::cout << "Approx Integral: " << point[0] << ", given n: " << point[1] << std::endl;
		}
	}
	return c_n;
}
int main(int argc, char *argv[]) {
	std::vector<std::array<double, 2>> c_n = simulate(f1, 5, 0, 8, 2); //choose funcion (f1, f2, f3, pi), k, a, b, M here
	file.close();
	return 0;
}

