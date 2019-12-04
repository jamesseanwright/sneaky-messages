# This is an implementation of
# http://www.ijera.com/papers/Vol2_issue4/AZ24339344.pdf

import math
import numpy

magic = [13, 91, 11, 12, 78, 37, 77, 17]
magic_len = len(magic)

def swap(shuffled, k, x):
  if (shuffled[k] != shuffled[x]):
    shuffled[x] = shuffled[k] + shuffled[x]
    shuffled[k] = shuffled[x] - shuffled[k]
    shuffled[x] = shuffled[x] - shuffled[k]

def shuffle(data):
  x = 1
  shuffled = list.copy(data)
  data_len = len(data)

  for j in range(0, magic_len):
    for k in range(0, data_len):
      x = ((j + 2) * x + magic[(j + k + 1) % magic_len]) % data_len
      swap(shuffled, k, x)

  return shuffled

def build_data_matrix(shuffled):
  shuffled_len = len(shuffled)
  n = math.ceil(math.sqrt(shuffled_len))
  filled = shuffled + [0] * (n ** 2 - shuffled_len)

  return numpy.reshape(numpy.array(filled), (n, n))
