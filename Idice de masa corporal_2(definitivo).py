print ('vamos a saber tu indice de masa corporal')

weight = float(input('ingrese su peso en kilogramos: '))
height = float(input('ingrese su altura en metros asi(1.70): '))

bmi = (weight/height ** 2)

print ('tu indice de masa corporal es: ', round(bmi, 2) )


#revisa el valor de bmi y dependiendo de su valor arroja que indice de masa tiene el usuario

if 0>=bmi<=18.5:
  print ('estas por debajo de tu peso')
elif bmi>=18.6 and bmi<=25:
  print ('tienes un peso normal')
elif bmi>=25.1 and bmi<=30:
  print ('tienes sobrepeso')
elif bmi>=30.1 and bmi<=35:
  print ('eres obeso')
elif bmi>=35.1:
  print ('clinicamente obeso')









