import java.util.List;
import java.util.ArrayList;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class Solution {
    public int getDecimalValue(ListNode head) {
        List<Integer> number = new ArrayList<>();

        while (head != null) {
            number.add(head.val);
            head = head.next;
        }

        int result = 0;
        int base = 0;
        for (int i = number.size() - 1; i >= 0; i--) {
            if (number.get(i) == 0) {
                continue;
            }
            result += Math.pow(2, base);
            base++;
        }
        return result;
    }
}
