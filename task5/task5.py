def task(str1,str2):
  import json
  import numpy as np
  import nums_from_string
  dataA = json.loads(str1)
  dataB = json.loads(str2)
  def mas(A):
    #print(A)
    #print(nums_from_string.get_nums(A))
    numbers = []
    for item in A:
      #print(item)
      try:
        numbers.append(int(item))
      except:
        mass=[]
        for i in range(len(item)):
          mass.append(int(item[i]))
        numbers.append(mass)
    return numbers

  def get_table(numbers):
    max=0
    for elem in numbers:
      try:
        if elem>max:
          max=elem
      except:
        for i in elem:
          if i>max:
            max=i
    table = np.zeros((max,max))
    mas=np.zeros(max)
    for item in numbers:
      try:
        mas[item-1]=1
        for j in range(max):
          if mas[j]==0:
            table[j,item-1]=0
          else:
            table[j,item-1]=1
      except:
        for elem in item:
          mas[elem-1]=1
        for elem in item:
          for j in range(max):
            if mas[j]==0:
              table[j,elem-1]=0
            else:
              table[j,elem-1]=1
    return table

  def back_string(arg):
    estimated=[]
    for item in arg:
      try:
        estimated.append(str(item+1))
      except:
        mas=[]
        for elem in item:
          mas.append(str(elem+1))
        estimated.append(mas)
    return estimated

  dataA=mas(dataA)
  dataB=mas(dataB)
  tableA=get_table(dataA)
  tableB=get_table(dataB)
  mergedTable=tableA*tableB+tableA.T*tableB.T

  answer=[]

  for j in range(mergedTable.shape[1]):
    for i in range(j):
      if mergedTable[i,j]==0:
        answer.append([i,j])

  return back_string(answer)