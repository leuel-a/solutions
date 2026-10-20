#include <string>

using std::string;

class Solution
{
  public:
	int strStr(string haystack, string needle)
	{
		int N = haystack.length();
		int M = needle.length();

		for (int i = 0; i < N; i++) {
			string current;

			for (int j = i; (j - i + 1) <= M && j < N; j++) {
				current.push_back(haystack.at(j));
			}

			if (current.compare(needle) == 0) {
				return i;
			}
		}

		return -1;
	}
};
