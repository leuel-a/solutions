#include <stdlib.h>

int comp(const void *a, const void *b)
{
	int x = *(const int *)a, y = *(const int *)b;
	return x == y ? 0 : x < y ? -1 : 1;
}

long long maxAlternatingSum(int *nums, int n)
{
	long long sum = 0;
	int *squares = malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++)
	{
		squares[i] = (nums[i] * nums[i]);
	}

	qsort(squares, n, sizeof(squares[0]), comp);

	for (int i = 0; i < n / 2; i++)
	{
		sum -= squares[i];
	}

	for (int i = n / 2; i < n; i++)
	{
		sum += squares[i];
	}

	return sum;
}
