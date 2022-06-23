import pytest


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_char_count = {}
        for ransom_note_char in ransomNote:
            ransom_note_char_count[ransom_note_char] = ransom_note_char_count.get(ransom_note_char, 0) + 1
        magazine_char_count = {}
        for magazine_char in magazine:
            magazine_char_count[magazine_char] = magazine_char_count.get(magazine_char, 0) + 1
        for ransom_char, char_count in ransom_note_char_count.items():
            if ransom_char not in magazine_char_count:
                return False
            if char_count > magazine_char_count[ransom_char]:
                return False
        return True


@pytest.mark.parametrize(
    'ransom_note, magazine, expected_result', [
        ('a', 'b', False),
        ('aa', 'a', False),
        ('a', 'ab', True),
        ('abcd', 'aabcdd', True),
        ('abcdd', 'abcd', False),
    ]
)
def test_solution(ransom_note, magazine, expected_result):
    assert Solution().canConstruct(ransom_note, magazine) == expected_result
