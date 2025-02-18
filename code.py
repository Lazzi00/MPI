
import math

# Constantes
pi = 3.14
w0 = 1
f = 0
aL = 0.01
h = 0.01
w = 1

    

# Fonction pour calculer l'accélération angulaire
def g(t, theta, v):
    return -w0**2 * math.sin(theta) - aL * v + f * math.cos(w * t)

# Fonction pour retourner la vitesse
def f_func(t, theta, v):
    return v

# Initialisation des variables
t = 0.0
theta = pi / 5
v = 0
T = 2 * pi / w0

# Ouverture du fichier pour l'écriture
with open("pendule_eul.txt", "w") as fp:
    print(f"{t} {theta} {v}")
    fp.write(f"{t} {theta} {v}\n")

    # Boucle d'itération
    t = h
    while t <= 3 * T:
        theta = theta + h * f_func(t, theta, v)
        v = v + h * g(t, theta, v)
        print(f"{t} {theta} {v}")
        fp.write(f"{t} {theta} {v}\n")
        t += h
