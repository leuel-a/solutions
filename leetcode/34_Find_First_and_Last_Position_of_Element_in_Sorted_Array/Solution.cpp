#include <vector>

using std::vector;

class Solution
{
  public:
	vector<int> searchRange(vector<int> &nums, int target)
	{
		vector<int> result(2, -1);

		if (nums.size() == 0) {
			return result;
		}

		// largest element smaller than target
		int i = -1, j = nums.size();
		while (i + 1 < j) {
			int middle = i + (j - i) / 2;

			if (nums.at(middle) < target) {
				i = middle;
			} else {
				j = middle;
			}
		}

		if (j == nums.size() || nums.at(j) != target) {
			return result;
		}

		result[0] = j;

		// smallest element greater than target
		i = -1, j = nums.size();
		while (i + 1 < j) {
			int middle = i + (j - i) / 2;

			if (nums.at(middle) <= target) {
				i = middle;
			} else {
				j = middle;
			}
		}

		result[1] = i;

		return result;
	}
};
