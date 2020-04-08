def front_back(str):
  front = str[0:1]
  back = str[len(str) - 1 :len(str)]
  a = str[1:len(str) - 1]
  if len(str) == 1:
    return str
  return back + a + front
