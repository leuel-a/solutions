#include <functional>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>

using std::greater;
using std::make_pair;
using std::pair;
using std::priority_queue;
using std::vector;

void tc()
{
	int N, M;
	std::cin >> N >> M;

	vector<vector<pair<long long, long long>>> graph(N, vector<pair<long long, long long>>{});
	for (int i = 0; i < M; i++) {
		long long a, b, w;
		std::cin >> a >> b >> w;
		--a;
		--b;
		graph[a].push_back(make_pair(w, b));
	}

	const long long __INF = 1e18;
	vector<long long> d(N, __INF);
	priority_queue<
		pair<long long, int>,
		vector<pair<long long, int>>,
		greater<pair<long long, int>>>
		pq;

	int start = 0;
	d[start] = 0;
	pq.push(make_pair(0, start));

	while (!pq.empty()) {
		auto [current_weight, current] = pq.top();
		pq.pop();

		if (current_weight != d[current]) {
			continue;
		}

		for (auto [weight, neighbour] : graph[current]) {
			if (weight + current_weight < d[neighbour]) {
				d[neighbour] = weight + current_weight;
				pq.push(make_pair(d[neighbour], neighbour));
			}
		}
	}

	for (int i = 0; i < N; ++i) {
		if (i != 0) {
			std::cout << " ";
		}
		std::cout << d[i];
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
