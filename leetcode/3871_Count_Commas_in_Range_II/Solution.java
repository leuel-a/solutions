// https://leetcode.com/problems/count-commas-in-range-ii

class Solution {
    public long countCommas(int num) {
        long power = 1000, result = 0;
        while (power <= num) {
            result += num - power + 1;
            power *= 1000;
        }
        return result;
    }
}
