# mutiples of 3 : HOP
# mutiples of 5 : VIZ
# multiples of 3 and 5 : HOPVIZ

# My solutions

for number in range(1,100):
    print('{:>5}'.format('HOP...VIZ' if number%15==0 else 'HOP' if number%3==0 else 'Viz' if number%5==0 else number))
# Teacher's

for number in range(1,100):
    decision= 'HOP...VIZ' if not number%15 else 'HOP' if not number%3 else 'Viz' if not number%5 else str(number)
    print(decision)
# نکته: اینکه از 3 شروع شد علتش اینه که بیشترین تعداد رو داریم
# از If not بجای ==
# چون نوع داده number  استرینگ شد پس تابع str را آوردیم و Explicit is Better than Impl

# version control software >>> کد را از جایی که درست کار میکنه نمایش میده برای کارهای تیمی بسیار لازمه
# to use version control we sign up in github afterthat we can use it as repasitory
