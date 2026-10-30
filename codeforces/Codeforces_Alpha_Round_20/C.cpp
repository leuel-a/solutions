#include <iostream>
#include <queue>
#include <utility>
#include <vector>

// using std::make_pair;
using std::pair;
using std::priority_queue;
using std::vector;

void tc()
{
	int N, M;
	std::cin >> N >> M;

	vector<vector<pair<int, int>>> graph(N, vector<pair<int, int>>{});
	for (int i = 0; i < M; i++) {
		int a, b, w;
		std::cin >> a >> b >> w;
		--a;
		--b;

		graph[a].push_back({w, b});
		graph[b].push_back({w, a});
	}

	const long long __INF = 1e18;
	int start = 0;
	vector<long long> d(N, __INF);
	vector<int> p(N, -1);
	priority_queue<
		pair<long long, int>,
		vector<pair<long long, int>>,
		std::greater<pair<long long, int>>>
		pq;

	d[start] = 0;
	pq.push({0, start});
	while (!pq.empty()) {
		auto [current_weight, v] = pq.top();
		pq.pop();

		if (current_weight > d[v]) { // stale
			continue;
		}

		for (auto [weight, neighbour] : graph[v]) {
			if (weight + current_weight < d[neighbour]) {
				d[neighbour] = weight + current_weight;
				p[neighbour] = v;
				pq.push({d[neighbour], neighbour});
			}
		}
	}

	if (d[N - 1] == __INF) {
		std::cout << -1 << std::endl;
		return;
	}

	vector<int> path;
	for (int i = N - 1; i != -1; i = p[i]) {
		path.push_back(i);
	}

	int K = path.size();
	for (int i = K - 1; i >= 0; --i) {
		if (i != K - 1) {
			std::cout << " ";
		}
		std::cout << path[i] + 1;
	}
	std::cout << "\n";
}

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL);

	tc();

	return (0);
}
