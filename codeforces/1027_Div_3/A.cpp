#include <iostream>

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL);

	int t;
	std::cin >> t;

	while (t--) {
		int year;
		std::cin >> year;

		int l = 0, r = 10000;
		while (l < r) {
			int m = l + (r - l) / 2;

			if (m * m > year) {
				r = m - 1;
			} else if (m * m < year) {
				l = m + 1;
			} else {
				l = m, r = m;
			}
		}

		if (l * l == year) {
			std::cout << l << " " << 0 << std::endl;
		} else {
			std::cout << -1 << std::endl;
		}
	}

	return (0);
}
