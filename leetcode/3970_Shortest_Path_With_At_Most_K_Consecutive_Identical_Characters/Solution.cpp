#include <climits>
#include <functional>
#include <queue>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using std::greater;
// using std::make_pair;
using std::pair;
using std::priority_queue;
using std::string;
using std::tuple;
using std::vector;

class Solution
{
  public:
	int shortestPath(int n, vector<vector<int>> &edges, string labels, int k)
	{
		vector<vector<pair<int, int>>> g(n); // pair<{edge, weight}>
		for (auto &e : edges) {
			int u = e[0], v = e[1], w = e[2];
			g[u].emplace_back(v, w);
		}

		vector dist(n, vector<long long>(k + 1, INT_MAX));

		// {shortest path length, node_index, num of consecutive identical letters}
		priority_queue<
			tuple<long long, int, int>,
			vector<tuple<long long, int, int>>,
			greater<>>
			pq;

		dist[0][1] = 0;
		pq.emplace(0, 0, 1);

		while (!pq.empty()) {
			auto [d, x, cnt] = pq.top();
            pq.pop();

            if (d > dist[x][cnt]) {
                continue;
            }

            if (x == n - 1) {
                return d;
            }

            for (auto [y, w]: g[x]) {
                int new_cnt = labels[x] == labels[y] ? cnt + 1 : 1;
                if (new_cnt > k) {
                    continue;
                }

                long long nd = d + w;
                if (nd < dist[y][new_cnt]) {
                    dist[y][new_cnt] = nd;
                    pq.emplace(nd, y, new_cnt);
                }
            }
		}

		return -1;
	}
};
