km = float(input('Quantos KM percorridos? '))
dias = int(input('Quantos dias alugado?'))
pagar = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${pagar:.2f}')
