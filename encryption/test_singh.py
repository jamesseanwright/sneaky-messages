# TODO: remove the tests for the
# implementation detail functions
# when the main API surface is done.
# These current tests enable us to
# ensure that we're following each
# step of the specification correctly.

import unittest
import numpy
import singh

class TestSingh(unittest.TestCase):
  def test_shuffle(self):
    message = 'Hello, world!'
    message_codes = [ord(char) for char in message]
    shuffled = singh.shuffle(message_codes)

    self.assertEqual(
      shuffled,
      [111, 108, 0, 119, 44, 0, 0, 0, 111, 33, 0, 0, 72],
    )

  def test_build_data_matrix(self):
    shuffled = [111, 108, 0, 119, 44, 0, 0, 0, 111, 33, 0, 0, 72]
    data_matrix = singh.build_data_matrix(shuffled)

    numpy.testing.assert_equal(
      data_matrix,
      numpy.array([
        [111, 108, 0, 119],
        [44, 0, 0, 0],
        [111, 33, 0, 0],
        [72, 0, 0, 0],
      ]),
    )
