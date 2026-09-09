// https://leetcode.com/problems/count-commas-in-range/description/

public class Solution {
    public int countCommas(int n) {
        String strN = String.valueOf(n);
        if (strN.length() < 4) {
            return 0;
        }

        int X = Integer.parseInt(strN.substring(0, strN.length() - 3));
        int N = Integer.parseInt(strN.substring(strN.length() - 3));

        return (X - 1) * 1000 + (N + 1);
    }
}
