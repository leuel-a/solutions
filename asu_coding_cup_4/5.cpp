#include <algorithm>
#include <iostream>
#include <vector>

// PROBLEM https://codeforces.com/gym/102397/problem/E

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, x;
    std::cin >> n >> x;

    std::vector<int> prefix(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        std::cin >> prefix[i];
        prefix[i] += prefix[i - 1];
    }

    int result = -1;
    int i = 0, j = 1;
    while (j <= n) {
        while (prefix[j] - prefix[i] >= x) {
            result = (result == -1) ? j - i : std::min(result, j - i);
            i++;
        }
        j++;
    }

    std::cout << result << std::endl;
    return (0);
}
