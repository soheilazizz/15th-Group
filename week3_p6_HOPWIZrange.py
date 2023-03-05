#for number in range(1,100):
  #  decision= 'HOP...VIZ' if not number%15 else 'HOP' if not number%3 else 'Viz' if not number%5 else str(number)
#    print(decision)
for a in range(1,100):
    print('hop..viz' if a in range(0,100,15)
          else 'hop' if a in range(0,100,3)
          else 'viz' if a in range(0,100,5)
          else str(a))