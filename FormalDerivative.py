def FormalDerivative(Fx):
  return [(x[0] * x[1], x[1] - 1) for x in Fx if x[1] > 0]


def polyrep(Fx):
  s = ["%dx ^ %d" % x for x in Fx]
  return " + ".join(s)

fx = [(-1,6),(1,0)]
print(polyrep(fx))
fx = FormalDerivative(fx)
print(polyrep(fx))
