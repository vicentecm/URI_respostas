# URI 1020 https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

em_dias = int(input())

anos = em_dias//365
sobra_para_meses = em_dias%365
meses = sobra_para_meses//30
dias = sobra_para_meses%30
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')