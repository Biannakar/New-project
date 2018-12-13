import random
import local
while True:
  word = ''
  letters = ('А', 'Е', 'Н', 'О', 'С', 'Т')
  n = 1
  p = 0
  x = 0 #для выхода из бесконечного цикла 0
  right_sum = 0
  wrong_sum = 0
  while True:
    x_letter = random.choice(letters)
    if word.find(x_letter) == -1:
      word += x_letter
      x += 1
    if x == 4:
      break
  for k in range(10):
    print(local.guess)
    trying = str(input(local.attempt + str(n) + ':'))
    n += 1
    for d in range(4):
      if word.find(trying[p]) > -1:
        if word[p] == trying[p]:
          right_sum += 1
        elif trying.count(trying[p]) > 1:
          wrong_sum += 0
        else:
          wrong_sum += 1
      p += 1
    p = 0
    print(local.r_place, right_sum)
    print(local.w_place, wrong_sum)
    if right_sum == 4:
      print(local.win)
      break
    right_sum = 0
    wrong_sum = 0
  else:
    print(local.lose)
    print(local.hidden,word)
  again = input(local.choice)
  if again == 'стоп':
    break
  else:
    continue
print(local.thanks)