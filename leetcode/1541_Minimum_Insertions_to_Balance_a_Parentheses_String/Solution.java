import java.util.Stack;

class Solution {
    public int minInsertions(String s) {
        int minChanges = 0;
        char OPEN_PARENTHESES = '(', CLOSE_PARENTHESES = ')';
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == OPEN_PARENTHESES) {
                if (!stack.isEmpty() && stack.peek() == CLOSE_PARENTHESES) {
                    stack.pop(); // remove )
                    stack.pop(); // remove (
                    minChanges++;
                }
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    stack.push(OPEN_PARENTHESES);
                    minChanges++;
                    stack.push(CLOSE_PARENTHESES);
                } else {
                    if (stack.peek() == OPEN_PARENTHESES) {
                        stack.push(CLOSE_PARENTHESES);
                    } else {
                        stack.pop(); // remove )
                        stack.pop(); // remove (
                    }
                }
            }
        }

        if (!stack.isEmpty() && stack.peek() == CLOSE_PARENTHESES) {
            stack.pop(); // remove )
            stack.pop(); // remove (
            minChanges++;
        }

        return minChanges + (stack.size() * 2);
    }
}
