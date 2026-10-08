import java.util.Stack;

class Solution {
    public String removeOuterParentheses(String s) {
        Integer openCount = 0;
        Character OPEN_PARENTHESES = '(';
        Stack<Integer> stack = new Stack<>();
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == OPEN_PARENTHESES) {
                openCount++;
                stack.push(i);
            } else {
                if (openCount == 1) {
                    while (stack.size() > 1) {
                        stack.pop();
                    }

                    int j = stack.pop();
                    result.append(s, j + 1, i);
                } else {
                    stack.push(i);
                }
                openCount--;
            }
        }

        return result.toString();
    }
}
