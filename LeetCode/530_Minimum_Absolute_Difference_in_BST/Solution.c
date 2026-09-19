#include <limits.h>
#include <stdlib.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int count_nodes(struct TreeNode *node)
{
    if (node == NULL) {
        return 0;
    }

    int left = count_nodes(node->left);
    int right = count_nodes(node->right);
    return left + right + 1;
}

void inorder_traversal(struct TreeNode *node, int *numbers, int *index)
{
    if (node == NULL)
        return;

    inorder_traversal(node->left, numbers, index);
    numbers[*index] = node->val;
    (*index)++;
    inorder_traversal(node->right, numbers, index);
}

int getMinimumDifference(struct TreeNode *root)
{
    int n = count_nodes(root);
    int *numbers = calloc(n, sizeof(int));
    int result = INT_MAX;
    int index = 0;

    inorder_traversal(root, numbers, &index);

    for (int i = 1; i < n; i++) {
        result = MIN(numbers[i] - numbers[i - 1], result);
    }
    return result;
}
