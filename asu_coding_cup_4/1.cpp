#include <iostream>

// PROBLEM: https://codeforces.com/gym/102397/problem/A

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie();

	int sandwiches, COST_PER_SANDWICH = 2;
	std::cin >> sandwiches;

	std::cout << sandwiches * COST_PER_SANDWICH << std::endl;
	return (0);
}
