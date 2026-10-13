import java.util.Arrays;

class Solution {
    public long maxAlternatingSum(int[] nums) {
        long sum = 0;
        int[] squares = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            squares[i] = nums[i] * nums[i];
        }

        Arrays.sort(squares);

        int i = 0, j = squares.length - 1;
        while (i < j) {
            sum += (squares[j] - squares[i]);
            i++;
            j--;
        }

        if (i == j) {
            sum += squares[i];
        }

        return sum;
    }
}
