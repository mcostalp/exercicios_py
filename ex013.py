old_s = float(input('Digite o atual salário do funcionário: R$'))

aumento = old_s * 15/100
new_s = old_s + aumento

print('O funcionário que ganha R${:.2f} passará a ganhar R${:.2f} com 15% de aumento.'.format(old_s, new_s))
