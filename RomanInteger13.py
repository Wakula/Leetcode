import pytest


class Solution:
    VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    DESCENDING_SYMBOL = {
        'I': ['V', 'X'],
        'X': ['L', 'C'],
        'C': ['D', 'M'],
    }

    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0
        length = len(s)
        while i < length:
            cur_symbol = s[i]
            next_symbol_index = i + 1
            next_symbol = s[next_symbol_index] if next_symbol_index != length else None
            if cur_symbol not in self.DESCENDING_SYMBOL or next_symbol not in self.DESCENDING_SYMBOL[cur_symbol]:
                res += self.VALUES[cur_symbol]
            else:
                res += (self.VALUES[next_symbol] - self.VALUES[cur_symbol])
                i += 1
            i += 1
        return res


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("I", 1), ("II", 2),  ("III", 3), ('IV', 4), ('V', 5), ('VI', 6), ('VII', 7), ('VIII', 8), ('IX', 9), ('X', 10),
        ("XI", 11), ("XII", 12), ("XIII", 13), ("XIV", 14), ("XV", 15), ("XVI", 16), ("XVII", 17), ("XVIII", 18),
        ("XIX", 19), ("XX", 20), ('LVIII', 58), ("MCMXCIV", 1994), ("MMMCMXCIX", 3999)
    ]
)
def test_converts_roman(test_input, expected):
    res = Solution().romanToInt(test_input)
    assert res == expected
