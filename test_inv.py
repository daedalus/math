from gmpy2 import invert
from timing import timing

@timing
def compute_modinv_1_n(n, p):
  """
  https://codeforces.com/blog/entry/83075
  """
  inv = [0, 1]
  inv.extend((p - p // i) * inv[p % i] % p for i in range(2, n))
  return inv

@timing
def compute_modinv_gmpy_1_n(n, p):
  inv = [0]
  inv.extend(int(invert(i, p)) for i in range(1, n))
  return inv


n, p = 10**4, 10**9+7
#n, p = 10, 65537

a = compute_modinv_1_n(n, p)
b = compute_modinv_gmpy_1_n(n, p)


