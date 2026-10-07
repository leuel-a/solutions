import java.util.HashMap;

class Solution {
    public boolean isHappy(int n) {
        HashMap<String, String> seen = new HashMap<>();
        String previous = String.valueOf(n);
        Boolean repeated = false;

        while (repeated == false) {
            int sum = 0;
            String current = String.valueOf(previous);
            for (char num : current.toCharArray()) {
                int value = num - '0';
                sum += (value * value);
            }

            current = String.valueOf(sum);

            if (seen.get(previous) != null) {
                repeated = true;
            }

            seen.put(previous, current);
            previous = current;
        }

        return Integer.valueOf(previous) == 1;
    }
}
