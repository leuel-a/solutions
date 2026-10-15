class Solution {
    public String maxSumOfSquares(int num, int sum) {
        if (sum > 9 * num) {
            return "";
        }

        StringBuilder result = new StringBuilder();
        int remainder = sum % 9;

        for (int i = 0; i < (sum / 9); i++) {
            result.append('9');
        }

        if (remainder > 0) {
            result.append((char) (remainder + '0'));
        }

        int zeros = num - result.length();
        for (int i = 0; i < zeros; i++) {
            result.append('0');
        }

        return result.toString();
    }
}
