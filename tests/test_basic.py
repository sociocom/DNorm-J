# -*- coding: utf-8 -*-

import unittest

from .context import M

QUERIES = ["腸閉塞症状", "高Ｃａ尿症", "二次性副腎不全"]
ANSWERS = ["イレウス", "高カルシウム尿症", "副腎クリーゼ"]


class BasicTestSuite(unittest.TestCase):
    """Input-Output Testing."""

    def test_query(self):
        for q, a in zip(QUERIES, ANSWERS):
            assert M.normalize(q) == a


if __name__ == "__main__":
    unittest.main()
