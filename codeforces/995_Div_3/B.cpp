#include <iostream>

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL);

	int t;
	std::cin >> t;

	while (t--) {
		long long n, a, b, c;

		std::cin >> n >> a >> b >> c;

		long long lo = 1;
		long long hi = 1000000000;

		while (lo < hi) {
			long long mid = lo + (hi - lo) / 2;
			long long distance = (mid / 3) * (a + b + c);
			int remainder = mid % 3;

			if (remainder == 1) {
				distance += a;
			} else if (remainder == 2) {
				distance += (a + b);
			}

			if (distance >= n) {
				hi = mid;
			} else {
				lo = mid + 1;
			}
		}

		std::cout << lo << std::endl;
	}

	return (0);
}
