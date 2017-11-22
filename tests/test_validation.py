import unittest
from launchkey.exceptions import LaunchKeyAPIException


class TestLaunchKeyAPIException(unittest.TestCase):

    def test_no_input(self):
        e = LaunchKeyAPIException()
        self.assertIsNone(e.message)
        self.assertIsNone(e.status_code)
        self.assertIsNone(e.reason)
        self.assertIsNone(e.error_code)

    def test_message(self):
        e = LaunchKeyAPIException(message="A Message")
        self.assertEqual(e.message, "A Message")
        self.assertIsNone(e.status_code)
        self.assertIsNone(e.reason)
        self.assertIsNone(e.error_code)

    def test_status_code(self):
        e = LaunchKeyAPIException(status_code=200)
        self.assertIsNone(e.message)
        self.assertEqual(e.status_code, 200)
        self.assertIsNone(e.reason)
        self.assertIsNone(e.error_code)

    def test_reason(self):
        e = LaunchKeyAPIException(reason="A Reason")
        self.assertIsNone(e.message)
        self.assertIsNone(e.status_code)
        self.assertEqual(e.reason, "A Reason")
        self.assertIsNone(e.error_code)

    def test_error_code_from_message(self):
        e = LaunchKeyAPIException(message={"error_code": "A-1234"})
        self.assertEqual(e.message, {"error_code": "A-1234"})
        self.assertIsNone(e.status_code)
        self.assertIsNone(e.reason)
        self.assertEqual(e.error_code, "A-1234")
