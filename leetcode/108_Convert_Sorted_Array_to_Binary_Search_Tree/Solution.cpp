#include <vector>

using std::vector;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;

	TreeNode() : val(0), left(nullptr), right(nullptr) {}

	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

	TreeNode(int x, TreeNode *left, TreeNode *right)
		: val(x), left(left), right(right)
	{
	}
};

class Solution
{
  public:
	TreeNode *createNode(int val, TreeNode *left, TreeNode *right)
	{
		return new TreeNode(val, left, right);
	}

	TreeNode *build(int low, int high, vector<int> nums)
	{
		if (low > high) {
			return nullptr;
		}

		int middle = (low + high) / 2;

		return createNode(nums.at(middle), build(low, middle - 1, nums),
						  build(middle + 1, high, nums));
	}

	TreeNode *sortedArrayToBST(vector<int> &nums)
	{
		return build(0, nums.size() - 1, nums);
	}
};
