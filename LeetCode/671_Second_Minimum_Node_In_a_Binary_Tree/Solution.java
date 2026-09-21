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
    int minimumValue;
    long answer = Long.MAX_VALUE;

    public void findSecondMinimumValueHelper(TreeNode root) {
        if (root == null)
            return;

        if (minimumValue < root.val && root.val < answer) {
            answer = root.val;
        } else {
            findSecondMinimumValueHelper(root.left);
            findSecondMinimumValueHelper(root.right);
        }
    }

    public int findSecondMinimumValue(TreeNode root) {
        minimumValue = root.val;
        findSecondMinimumValueHelper(root);
        return answer == Long.MAX_VALUE ? -1 : (int) answer;
    }
}
