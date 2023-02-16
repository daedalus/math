def bpp(g,w):
  """
  Compute the probability of all elements in group g in the whole set w to have unique birthdays.
  """
  proba = 1
  for i in range(w, w - g, -1):
    proba *= (i/w)
  return proba


print(bpp(23,365))
