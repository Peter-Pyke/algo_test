"""number of facilities, number of customers, facilities fixed costs,
 customer demands, facilty capacities, transportation costs"""


f1 = 17391/7936   # 2.19
f2 = 122740/5931  # 20.69
f3 = 233153/7499  # 31.09
f4 = 205967/9643  # 21.35
f5 = 234507/9556  # 24.54
f6 = 42050/8585   # 4.89
f7 = 90581/11130  # 8.13
f8 = 230641/8229  # 28.02
f9 = 52511/7316   # 7.17
f10 = 103429/11935  # 8.66
F = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
F_in_order = sorted(F, reverse=True)  # f3, f8, f5, f4, f2, f10, f7, f9, f6, f1
print(F_in_order)
print(F)
