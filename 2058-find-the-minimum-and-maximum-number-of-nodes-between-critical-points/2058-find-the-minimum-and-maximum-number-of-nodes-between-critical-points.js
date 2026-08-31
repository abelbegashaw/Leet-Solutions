/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number[]}
 */
var nodesBetweenCriticalPoints = function(head) {
    let prev = head;
    let curr = head.next;
    let first_occurrence = -1;
    let last_occurrence = -1
    let result = [Infinity, -Infinity];
    let index = 1;
    while (curr.next) {
        let maxima = prev.val < curr.val && curr.val > curr.next.val;  
        let minima = prev.val > curr.val && curr.val < curr.next.val;
        console.log(maxima, minima)
        if (maxima || minima) {
            console.log(index);
            if (last_occurrence === -1) {
                first_occurrence = index;
            } else {
                result[0] = Math.min(result[0], index - last_occurrence);
                result[1] = index - first_occurrence;
            }
            last_occurrence = index;
        }

        prev = curr
        curr = curr.next;
        index++;
    }

    return result[0] !== Infinity ? result : [-1, -1];
};