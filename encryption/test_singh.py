# TODO: remove the tests for the
# implementation detail functions
# when the main API surface is done.
# These current tests enable us to
# ensure that we're following each
# step of the specification correctly.

import unittest
import singh

class TestSingh(unittest.TestCase):
  def test_shuffle(self):
    message = 'Hello, world!'
    message_codes = [ord(char) for char in message]
    shuffled = singh.shuffle(message_codes)

    self.assertEqual(
      [111, 108, 0, 119, 44, 0, 0, 0, 111, 33, 0, 0, 72],
      shuffled,
    )
