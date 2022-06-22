from typing import Optional

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palindrome_candidate = []
        i = head
        while i:
            palindrome_candidate.append(i.val)
            i = i.next
        candidate_length = len(palindrome_candidate)
        half_length = candidate_length // 2
        if palindrome_candidate[:half_length + candidate_length % 2] == list(reversed(palindrome_candidate[half_length:])):
            return True
        return False


@pytest.mark.parametrize(
    'test_input,expected', [
        ([1], True),
        ([1, 2], False),
        ([1, 2, 2, 1], True),
        ([1, 2, 1], True)
    ]
)
def test_solution(test_input, expected):
    head = ListNode(val=test_input[0])
    cur_node = head
    for i in test_input[1:]:
        new_node = ListNode(val=i)
        cur_node.next = new_node
        cur_node = new_node

    assert Solution().isPalindrome(head) == expected
