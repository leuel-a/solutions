#include <algorithm>
#include <vector>

using std::vector;

class Solution
{
  public:
	vector<int> targetIndices(vector<int> &nums, int target)
	{
		vector<int> indices;

		sort(nums.begin(), nums.end());

		for (int i = 0; i < nums.size(); i++) {
			if (nums.at(i) == target) {
				indices.push_back(i);
			}
		}

		return indices;
	}
};
