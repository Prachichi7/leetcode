class Solution {
    private List<Integer> sortedValues = new ArrayList<>();

    public TreeNode balanceBST(TreeNode root) {
        inorderTraversal(root);

        return buildBalancedBST(0, sortedValues.size() - 1);
    }


    private void inorderTraversal(TreeNode node) {
        if (node == null) {
            return;
        }
      
        inorderTraversal(node.left);
        sortedValues.add(node.val);
        inorderTraversal(node.right);
    }

    private TreeNode buildBalancedBST(int left, int right) {
        if (left > right) {
            return null;
        }
      
        int middleIndex = (left + right) >> 1; 
      
        TreeNode leftSubtree = buildBalancedBST(left, middleIndex - 1);
        TreeNode rightSubtree = buildBalancedBST(middleIndex + 1, right);
    
        return new TreeNode(sortedValues.get(middleIndex), leftSubtree, rightSubtree);
    }
}
