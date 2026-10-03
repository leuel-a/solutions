import java.util.List;
import java.util.ArrayList;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public int getMinimumDifference(TreeNode root) {
        List<Integer> numbers = new ArrayList<>();

        inOrderTraversal(root, numbers);

        int min = Integer.MAX_VALUE;
        for (int i = 1; i < numbers.size(); i++) {
            min = Math.min(numbers.get(i) - numbers.get(i - 1), min);
        }
        return min;
    }

    public void inOrderTraversal(TreeNode root, List<Integer> numbers) {
        if (root == null)
            return;

        inOrderTraversal(root.left, numbers);
        numbers.add(root.val);
        inOrderTraversal(root.right, numbers);
    }
}
