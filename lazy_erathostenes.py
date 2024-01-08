from itertools import islice


def nats(n):
    yield n
    yield from nats(n + 1)


def sieve(s):
    # print("sieve",s)
    n = next(s)
    yield n
    yield from sieve(i for i in s if i % n != 0)


print((list(islice(sieve(nats(2)), 30))))
