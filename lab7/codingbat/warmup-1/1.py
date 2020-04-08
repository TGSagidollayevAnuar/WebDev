def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
weekday = bool(input())
vacation = bool(input())
print(sleep_in(weekday, vacation))