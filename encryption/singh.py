import math
import numpy

magic = [13, 77, 92, 108, 119, 181, 203, 261]
magic_len = len(magic)

def swap(data, i, j):
  data[j] = data[i] + data[j]
  data[i] = data[j] - data[i]
  data[j] = data[j] - data[i]

def shuffle(data):
  x = 1
  shuffled = list.copy(data)
  data_len = len(data)

  for j in range(0, magic_len):
    for k in range(0, data_len):
      x = ((j + 1) * x + magic[(j + k) % magic_len]) % data_len
      swap(shuffled, k, x)

  return shuffled

def build_data_matrix(shuffled):
  shuffled_len = len(shuffled)
  n = math.ceil(math.sqrt(shuffled_len))
  filled = shuffled + [0] * (n ** 2 - shuffled_len)

  return numpy.reshape(numpy.array(filled), (n, n))
