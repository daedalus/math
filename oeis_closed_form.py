from sage.all import *
import sys
import json
import requests
import sqlite3


def getSequence(id):
    f = requests.get(f"https://oeis.org/search?fmt=json&q=id:{id}")
    doc = json.loads(f.content)
    return [int(x) for x in doc["results"][0]["data"].split(",")]


def guessSequence(lst):
    C = CFiniteSequences(QQ)
    if (s := C.guess(lst)) == 0:
        return
    else:
        return s.closed_form()


def checkSequence(id, items=10):
    data = getSequence(id)
    seq = data[:items]
    print((id, seq))
    if len(seq) > 7 and (r := guessSequence(seq)) is not None:
        seq = data[: items * 5]
        return guessSequence(seq)


def procfile():
    IDS = [line.rstrip() for line in open(sys.argv[1], "r").readlines()]
    for id in IDS:
        print((id, getSequence(id)))


def proc2():
    # conn = sqlite3.connect('oeis.db')
    # cur = conn.cursor()
    # cur.execute("CREATE TABLE sequence(id, name,data,formula)")
    # for row in cur.execute("SELECT id,name,data,formula FROM sequence ORDER BY id"):
    n = 1
    while True:
        id = "A%06d" % n
        print((id, checkSequence(id)))
        n += 1


proc2()
# procfile()
