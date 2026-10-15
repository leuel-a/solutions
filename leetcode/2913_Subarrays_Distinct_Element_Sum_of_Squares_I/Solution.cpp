#include <cstdio>
#include <set>
#include <vector>

using std::set;
using std::vector;

class Solution
{
  public:
	int sumCounts(vector<int> &nums)
	{
		int sum = 0;
		int distinctCount = 0;
		set<int> unique = {};

		for (auto i = nums.begin(); i != nums.end(); i++)
		{
			for (auto j = i; j != nums.end(); j++)
			{
				unique.insert(*j);
				distinctCount = unique.size();

				sum += (distinctCount * distinctCount);
			}

			unique.clear();
		}

		return sum;
	}
};
