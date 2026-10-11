/**
 * sumOfSquares - finds the sum of squares of special elements
 *
 * Description: You are given a 1-indexed integer array nums of length n.
 *				An element nums[i] of nums is called special if i divides n,
 *				i.e. n % i == 0.
 *
 * @nums: the array of integers
 * @numsSize: the size of the array of integers
 *
 * Return: the sum of the squares of the special elements
 */
int sumOfSquares(int *nums, int numsSize)
{
	int result = 0;

	for (int i = 0; i < numsSize; i++)
	{
		if (numsSize % (i + 1) == 0)
		{
			result += (nums[i] * nums[i]);
		}
	}

	return result;
}
