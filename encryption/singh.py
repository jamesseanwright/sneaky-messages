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

  for j in range(1, magic_len + 1):
    for k in range(1, data_len + 1):
      x = ((j + 1) * x + magic[(j + k) % magic_len]) % data_len
      swap(shuffled, k, x)

  shuffled
