import java.util.Set;
import java.util.HashSet;
import java.util.List;

class Solution {
    public int sumCounts(List<Integer> nums) {
        int sum = 0;
        int distinctCount = 0;
        Set<Integer> unique = new HashSet<>();

        for (int i = 0; i < nums.size(); i++) {
            for (int j = i; j < nums.size(); j++) {
                unique.add(nums.get(j));

                distinctCount = unique.size();
                sum += distinctCount * distinctCount;

            }

            unique.clear();
        }

        return sum;
    }
}
