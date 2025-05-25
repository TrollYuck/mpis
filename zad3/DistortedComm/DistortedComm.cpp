#include <iostream>
#include <fstream>
#include <array>
#include <random>
#include <vector>
#include <string>
#include <chrono>
#define _USE_MATH_DEFINES
#include <math.h>

static std::random_device rd;
static std::mt19937 mt(rd());
static std::uniform_real_distribution<double> dist(0.0, 1.0);
static std::ofstream ofs("distorted_comm05.csv");

std::vector<int> init_n_array() {
	int n = 100;
	std::vector<int> n_array;
	do {
		n_array.push_back(n);
		n += 100;
	} while (n <= 10000);
	return n_array;
}

int run_comm(int n, double p) {
	std::vector<int> knots(n, 0);
	int knots_communicated = 0;
	int T = 0;
	do {
		for (int knot : knots) {
			if (knot == 0) {
				double try_comm = dist(mt);
				if (try_comm <= p) {
					knot++;
					if (knot == 1) {
						knots_communicated++;
						if (knots_communicated == n)
							break;
					}
				}
			}
			T++;
		}
	} while (knots_communicated < n);
	return T;
}

void simulate(int k, double p) {
	std::vector<int> n_array = init_n_array();
	for (auto n : n_array) {
		std::cout << "n = " << n << " started." << std::endl;
		auto start = std::chrono::high_resolution_clock::now();
		for (int i = 0; i < k; i++) {
			int T = run_comm(n, p);
			ofs << n << "," << T << std::endl;
		}
		auto end = std::chrono::high_resolution_clock::now();
		std::chrono::duration<double> duration = end - start;
		std::cout << n << " ended in: " << duration.count() << std::endl;
	}
}

int main() {
	int k = 50;
	double p = 0.5;
	simulate(k, p);
	ofs.close();
	return 0;
}

