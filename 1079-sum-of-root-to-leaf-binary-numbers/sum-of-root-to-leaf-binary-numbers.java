/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumRootToLeaf(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int currentbinval) {
        if (node == null) {
            return 0;
        }
      
        currentbinval = (currentbinval << 1) | node.val;
      
        if (node.left == null && node.right == null) {
            return currentbinval;
        }
    
        return dfs(node.left, currentbinval) + dfs(node.right, currentbinval);
    }
}