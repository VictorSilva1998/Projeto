from math import radians, sin, cos, tan

angulo = float (input ("Digite o ângulo: "))

seno = sin (radians (angulo))
print ("O ângulo de {} tem o SENO de {:.2}" .format (angulo, seno))

cosseno = cos (radians (angulo))
print ("O ângulo de {} tem o COSSENO de {:.2}" .format (angulo, cosseno))

tangente = tan (radians (angulo))
print ("O ângulo de {} tem o TANGENTE de {:.2}" .format (angulo, tangente))