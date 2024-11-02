from logic import Symbol, And, Or, Not, Implication, model_check

# Definir los símbolos
lluvia = Symbol("lluvia")
BBC = Symbol("BBC")
Unimayor = Symbol("Unimayor")

# Proposiciones dadas en la diapositiva
# Si no llueve, los estudiantes visitan BBC hoy
proposicion1 = Implication(Not(lluvia), BBC)

# Estudiantes visitaron BBC o Unimayor pero no ambos
proposicion2 = And(Or(BBC, Unimayor), Not(And(BBC, Unimayor)))

# Estudiantes visitaron Unimayor hoy
proposicion3 = Unimayor

# Base de conocimiento
base_conocimiento = And(proposicion1, proposicion2, proposicion3)

# Inferencias
print("¿Podemos inferir que los estudiantes visitaron BBC hoy?")
print("Respuesta:", model_check(base_conocimiento, BBC))

print("¿Podemos inferir que está lloviendo hoy?")
print("Respuesta:", model_check(base_conocimiento, lluvia))
