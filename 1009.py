#URI 1009

nome = input()
salario_fixo = float(input())
total_vendas = float(input())
total_salario = salario_fixo+(total_vendas*0.15)
print(f"TOTAL = R$ {total_salario:.2f}")