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

class Solution {
    public void inOrderTraversal(TreeNode node, List<Integer> numbers) {
        if (node == null) {
            return;
        }

        inOrderTraversal(node.left, numbers);
        numbers.add(node.val);
        inOrderTraversal(node.right, numbers);
    }

    public int minDiffInBST(TreeNode root) {
        List<Integer> numbers = new ArrayList<>();

        inOrderTraversal(root, numbers);

        int min = Integer.MAX_VALUE;
        for (int i = 1; i < numbers.size(); i++) {
            min = Math.min(min, numbers.get(i) - numbers.get(i - 1));
        }
        return min;
    }
}
