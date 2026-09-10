/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var averageOfSubtree = function(root) {

    var calculate = function(root) {
        if (!root) {
            return [0,0,0]
        }

        let fromLeft = calculate(root.left)
        let fromRight = calculate(root.right)
        
        let subSum = fromLeft[0] + fromRight[0] + root.val
        let nodeCount = fromLeft[1] + fromRight[1] + 1
        let subCount = fromLeft[2] + fromRight[2] + (Math.floor(subSum / nodeCount) === root.val)

        return [subSum, nodeCount, subCount]
    }

    return calculate(root).at(-1);   
};