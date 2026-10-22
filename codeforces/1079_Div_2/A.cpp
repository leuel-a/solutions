#include <iostream>

long long get_digit_sum(long long num)
{
	long long sum = 0;

	while (num > 0) {
		sum += num % 10;
		num /= 10;
	}

	return sum;
}

long long F(long long y)
{
	return y - get_digit_sum(y);
}

long long findFirstGreaterElement(long long x, long long target)
{
	long long lo = x;
	long long hi = x + 200;

	while (lo < hi) {
		long long mid = lo + (hi - lo) / 2;

		if (F(mid) >= target) {
			hi = mid;
		} else {
			lo = mid + 1;
		}
	}

	return lo;
}

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL);

	int t;
	std::cin >> t;

	while (t--) {
		long long x;

		std::cin >> x;

		long long left = findFirstGreaterElement(x, x);
		long long right = findFirstGreaterElement(x, x + 1);

		std::cout << right - left << std::endl;
	}

	return (0);
}
