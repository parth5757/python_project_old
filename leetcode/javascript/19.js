/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    // Step 1: Initialize two pointers, p1 and p2, both pointing to the head node
    let p1 = head, p2 = head;

    // Step 2: Move p2 n steps ahead
    for (let i = 0; i < n; i++) {
        p2 = p2.next;
    }

    // Step 3: If p2 is null, it means we need to remove the head node
    if (p2 === null) {
        head = head.next;
        return head;
    }

    // Step 4: Move p1 and p2 together until p2 reaches the end of the list
    while (p2.next !== null) {
        p1 = p1.next;
        p2 = p2.next;
    }

    // Step 5: Remove the nth node from the end of the list
    p1.next = p1.next.next;

    return head;
};
