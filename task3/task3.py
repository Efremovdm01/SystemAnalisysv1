import csv
from io import StringIO

def classify(cons):
    t1 = list()
    t2 = list()
    t3 = list()
    t4 = list()
    t5 = list()
    for con in cons:
        t1.append(con)
        t2.append(con[::-1])
        for other_con in [c for c in cons if c != con]:
            if con[1] == other_con[0]:
                t3.append([con[0], other_con[1]])
                t4.append([other_con[1], con[0]])
            elif con[0] == other_con[0]:
                t5.append([con[1], other_con[1]])
    return t1, t2, t3, t4, t5

def task(csv_str):
    csv_io = StringIO(csv_str)
    reader = csv.reader(csv_io)
    data = list(reader)
    classes = classify(data)
    result = []
    for c in classes:
      result.append([])
      for pair in c:
        result[-1].append(int(pair[0]))
      result[-1] = list(set(result[-1]))
    return result