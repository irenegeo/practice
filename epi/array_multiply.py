def multiply(num1, num2):

  res = [0] * (len(num1) + len(num2))
  for i in reversed(range(len(num1))):
    for j in reversed(range(len(num2))):
      print num1[i]
      print num2[j]
      res[i+j +1] += num1[i] * num2[j]
      res[i + j] += res[i+j +1] // 10
      res[i + j + 1] %= 10
      print res
  print res
  print res[next((i for i,x in enumerate(res) if x !=0))]

multiply([1,1], [2,3])