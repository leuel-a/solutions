import java.util.Stack;

public class Solution {
    public boolean isValid(String s) {
        final char OPEN_PARENTHESES = '(', CLOSED_PARENTHESES = ')';
        final char OPEN_BRACE = '{', CLOSED_BRACE = '}';
        final char OPEN_BRACKET = '[', CLOSED_BRACKET = ']';

        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            switch (c) {
                case OPEN_PARENTHESES:
                case OPEN_BRACE:
                case OPEN_BRACKET:
                    stack.push(c);
                    break;
                case CLOSED_BRACE:
                    if (stack.isEmpty() || stack.peek() != OPEN_BRACE) {
                        return false;
                    }
                    stack.pop();
                    break;
                case CLOSED_PARENTHESES:
                    if (stack.isEmpty() || stack.peek() != OPEN_PARENTHESES) {
                        return false;
                    }
                    stack.pop();
                    break;
                case CLOSED_BRACKET:
                    if (stack.isEmpty() || stack.peek() != OPEN_BRACKET) {
                        return false;
                    }
                    stack.pop();
                    break;
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.isValid("()[]{}"));
    }
}
