import java.util.List;
import java.util.stream.Collectors;
import java.util.Arrays;

class Solution {
    public int minimumPairRemoval(int[] nums) {
        int count = 0;
        List<Integer> numbers = Arrays.stream(nums).boxed().collect(Collectors.toList());

        while (numbers.size() > 1) {
            boolean isAscending = true;
            int minSum = Integer.MAX_VALUE;
            int targetIndex = -1;

            for (int i = 0; i < numbers.size() - 1; i++) {
                int pairSum = numbers.get(i) + numbers.get(i + 1);

                if (numbers.get(i) > numbers.get(i + 1)) {
                    isAscending = false;
                }

                if (pairSum < minSum) {
                    minSum = pairSum;
                    targetIndex = i;
                }
            }

            if (isAscending == true) {
                break;
            }

            numbers.set(targetIndex, minSum);
            numbers.remove(targetIndex + 1);
            count++;
        }

        return count;
    }
}
