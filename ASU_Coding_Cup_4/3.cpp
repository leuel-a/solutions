#include <iostream>

// PROBLEM: https://codeforces.com/gym/102397/problem/C

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie();

    int x, y;
    std::string direction;

    std::cin >> x >> y;
    std::cin.clear();
    std::cin.ignore(10000, '\n');

    std::getline(std::cin, direction);

    for (char ch : direction) {
        switch (ch) {
        case 'U':
            y++;
            break;
        case 'D':
            y--;
            break;
        case 'L':
            x--;
            break;
        case 'R':
            x++;
            break;
        default:
            std::printf("direction not found");
            break;
        }
    }

    std::printf("%d %d\n", x, y);

    return (0);
}
