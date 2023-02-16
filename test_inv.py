from gmpy2 import invert


def compute_modinv_1_n(n, p):
  """
  https://codeforces.com/blog/entry/83075
  """
  inv = [0, 1]
  for i in range(2, n):
    inv.append((p - p // i) * inv[p % i] % p)
  return inv


def compute_modinv_gmpy_1_n(n, p):
  inv = [0]
  for i in range(1, n):
    inv.append(int(invert(i, p)))
  return inv


n, p = 10, 10**9+7
#n, p = 10, 65537

print(compute_modinv_1_n(n, p))
print(compute_modinv_gmpy_1_n(n, p))

