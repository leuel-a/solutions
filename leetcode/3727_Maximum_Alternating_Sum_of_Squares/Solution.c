#include <stdlib.h>

int comp(const void *a, const void *b)
{
	int x = *(const int *)a;
	int y = *(const int *)b;

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

	int i = 0, j = n - 1;
	while (i < j)
	{
		sum += (squares[j] - squares[i]);
		i++;
		j--;
	}

	if (i == j)
	{
		sum += squares[i];
	}

	return sum;
}
