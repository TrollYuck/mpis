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
static std::ofstream file_b("Bn.txt");
static std::ofstream file_c("Cn.txt");
static std::ofstream file_d("Dn.txt");
static std::ofstream file_u("Un.txt");

std::vector<int> init_n_array() {
	int n = 1000;
	std::vector<int> n_array;
	do {
		n_array.push_back(n);
		n += 1000;
	} while (n <= 100000);
	return n_array;
}

std::array<int, 4> throw_ball_into_bin(int n) {
	std::uniform_int_distribution<int> dist(0, n - 1);
	std::vector<int> bins(n, 0);
	std::array<int, 4> results = { 0, 0, 0, 0 };
	int B = 0; //pierwsza kolizja
	int C = 0; //wszystkie kosze zajete
	int D = 0; //wszystkie kosze maja co najmniej 2
	int U = 0; //liczba pustych koszy po n rzutach
	int U_count = n; //liczba pustych koszy
	int C_count = 0; //liczba zajetych koszy
	int i = 0; //liczba rzutow
	do {
		i++;
		int bin = dist(mt);
		bins[bin]++;
		if (bins[bin] == 2) {
			D++;
			if (D == 1) { //pierwsza kolizja
				B = i;
			}
		}
		if (bins[bin] == 1) {
			U_count--;
			C_count++;
			if (C_count == n) C = i;
		}
		if (i == n) U = U_count;
			
	} while (D < n);

	results[0] = B;
	results[1] = C;
	results[2] = i;
	results[3] = U;
	return results;
}

void sym(int n, int d) {
	std::uniform_int_distribution<> dist(0, n - 1);
	std::vector<int> bins(n, 0);
	std::vector<int> randBins;
	for (int i = 0; i < d; i++) {
		randBins.push_back(i);
	}
	int counter = 0;
	while (counter <= n) {
		counter++;
		for (int i = 0; i < d; i++) {
			randBins[i] = dist(mt);
		}
		int minBalls = bins[randBins[0]];
		int minIndex = randBins[0];
		for (int i = 1; i < d; i++) {
			if (bins[randBins[i]] < minBalls) {
				minBalls = bins[randBins[i]];
				minIndex = randBins[i];
			}
		}
		bins[minIndex]++;
	}
	int max = bins[0];
	for (int i = 1; i < n; i++) {
		if (bins[i] > max) {
			max = bins[i];
		}
	}
	file_d << n << " " << max << std::endl;
}

void print_results(int n, std::array<int, 4> results) {
	std::cout << "n = " << n << ", B = " << results[0] << ", C = " << results[1] << ", D = " << results[2] << ", U = " << results[3] << std::endl;
}

void write_results(int n, std::array<int, 4> results) {
	file_b << n << " " << results[0] << std::endl;
	file_c << n << " " << results[1] << std::endl;
	file_d << n << " " << results[2] << std::endl;
	file_u << n << " " << results[3] << std::endl;
}

void simulate(int n) {
	std::array<int, 4> results = throw_ball_into_bin(n);
	print_results(n, results);
	write_results(n, results);
}

void run_simulation(int k) {
	std::vector<int> n_array = init_n_array();
	//int n = 10000;
	for (auto n : n_array) {
		std::cout << "n = " << n << std::endl;
		for (int i = 0; i < k; i++) {
			//simulate(n);
			sym(n, 2); //d nalezy zmieniac dla a i b
		}
	}
}

int main() {
	int k = 50;
	run_simulation(k);
	file_b.close();
	file_c.close();
	file_d.close();
	file_u.close();
	return 0;
}