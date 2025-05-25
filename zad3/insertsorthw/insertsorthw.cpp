#include <iostream>
#include <fstream>
#include <array>
#include <random>
#include <vector>
#include <string>
#include <time.h>
#define _USE_MATH_DEFINES
#include <math.h>

static std::ofstream swap_file("swap.txt");
static std::ofstream cmp_file("cmp.txt");

std::vector<int> init_n_array() {
	int n = 100;
	std::vector<int> n_array;
	do {
		n_array.push_back(n);
		n += 100;
	} while (n <= 10000);
	return n_array;
}

std::vector<int> init_random_array(int n) {
	std::vector<int> random_array(n);
	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<> dis(1, n);
	for (int i = 0; i < n; i++) {
		random_array[i] = i + 1;
	}
	std::shuffle(random_array.begin(), random_array.end(), gen);
	return random_array;
}

void insertion_sort(std::vector<int>& arr, int n) {
	long cmp = 0;
	long swap = 0;
	for (int i = 1; i < n; i++) {
		int key = arr[i];
		int j = i - 1;
		while (j >= 0 && arr[j] > key) {
			cmp++;
			arr[j + 1] = arr[j];
			j = j - 1;
			swap++;
		}
		cmp++;
		arr[j + 1] = key;
	}
	cmp_file << n << " " << cmp << std::endl;
	swap_file << n << " " << swap << std::endl;
}

void run_simulation(int k) {
	std::vector<int> n_array = init_n_array();
	for (int n : n_array) {
		std::cout << "n = " << n << " sim started." << std::endl;
		for (int i = 0; i < k; i++) {
			std::vector<int> random_array = init_random_array(n);
			insertion_sort(random_array, n);
		}
		std::cout << "n = " << n << " FINISHED" << std::endl;
	}
}

int main()
{
	int k = 50;
	run_simulation(k);
	cmp_file.close();
	swap_file.close();
	return 0;
}

