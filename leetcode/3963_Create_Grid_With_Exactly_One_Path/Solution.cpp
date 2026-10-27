#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution
{
  public:
	vector<string> createGrid(int m, int n)
	{
		vector<string> result(m, string(n, '#'));

		result[0] = string(n, '.');
		for (int i = 1; i < m; i++) {
			result[i][n - 1] = '.';
		}
		return result;
	}
};
