valor_hora = 60.20
horas_trabalhadas = int(input("total horas trabalhadas mes"))
if horas_trabalhadas <=20:
	salario = horas_trabalhadas*valor_hora
	print(salario)
else:
	horas_extras =horas_trabalhadas - 20
	valor_extra = valor_hora * 0,3
	salario_extra = valor_hora*horas_trabalhadas+valor_hora*horas_extras
	print(salario_extra)
