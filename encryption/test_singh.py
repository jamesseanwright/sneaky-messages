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
    message = 'IT IS GENERALISED KEY' # from the whitepaper
    message_codes = [ord(char) for char in message]
    shuffled = singh.shuffle(message_codes)

    self.assertEqual(
      len(message_codes),
      len(shuffled)
    )

    self.assertEqual(
      shuffled,
      [84, 69, 76, 73, 65, 75, 68, 73, 73, 78, 83, 32, 69, 32, 83, 82, 89, 71, 69, 69, 32],
    )

  def test_build_data_matrix(self):
    shuffled = [84, 69, 76, 73, 65, 75, 68, 73, 73, 78, 83, 32, 69, 32, 83, 82, 89, 71, 69, 69, 32]
    data_matrix = singh.build_data_matrix(shuffled)

    numpy.testing.assert_equal(
      data_matrix,
      numpy.array([
        [84, 69, 76, 73, 65],
        [75, 68, 73, 73, 78],
        [83, 32, 69, 32, 83],
        [82, 89, 71, 69, 69],
        [32, 0, 0, 0, 0],
      ]),
    )

if __name__ == '__main__':
    unittest.main()