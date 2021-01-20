import unittest
import os
import sys
sys.path.insert(1, os.getcwd().removesuffix("test"))
from nelxte.username import check_username  # noqa : E402

# testing the username utility


class UsernameTests(unittest.TestCase):

    def test_for_swears(self):
        for swear in [
            "anal", "anus", "arse", "ass",
            "bastard", "bitch", "blowjob", "bloody"
        ]:
            self.assertEqual(
                check_username(swear),
                f"Inappropriate word : {swear} (and possibly more)"
                " detected in name",
                f"swear check has failed swear is {swear}"
            )

    def test_for_length(self):
        test_cases = ["a", "abc", "abc"*7]
        for test_case in test_cases:
            if len(test_case) <= 2:
                expected_result = f"the username, {test_case} (length is 1), is too small(min length = 2)"  # noqa: E501
            elif len(test_case) >= 256:
                expected_result = f"the username, {test_case} (length is 1), is too large(max length = 2)"  # noqa: E501
            else:
                expected_result = "OK"
            self.assertEqual(
                check_username(test_case),
                expected_result,
                f"{check_username(test_case)} not {expected_result}",
            )


if __name__ == "__main__":
    unittest.main()
