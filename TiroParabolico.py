# Integrantes del grupo:
# - Altobello, Juliana
# - Grassi, Antonella
# - Messana Gullielmi, Agustín

# Librerías necesarias para graficar la trayectoria en 3D
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# ? Para nuestro modelo tomaremos al eje y como eje vertical.
# Fórmulas a utilizar (tomadas del libro Sears and Zemansky's University Physics with Modern Physics 14th Edition, página 76).
# Se obtienen aplicando la ecuación vectorial de movimiento con aceleración constante r(t) = r0 + v0*t + 1/2*a*t^2.

# Eje X (MRU):
# x(t) = x0 + vx0 * t

# Eje Y (MRUV - Gravedad):
# y(t) = y0 + vy0 * t - 0.5 * g * t^2

# Eje Z (MRU - Análogo a X):
# z(t) = z0 + vz0 * t

# ! Aclaración: 
# en dicha página no se hace mención del movimiento en el eje z, así que lo razonamos de la siguiente manera:
# La única fuerza es el peso P = m*g, que sólo actúa en dirección vertical. Si definimos el eje vertical como y, tenemos:
# ax = 0, ay = -g, az=0 pues no hay fuerzas en x o en z.
# Entonces, si az = 0, el movimiento en z es rectilíneo uniforme como en x. De allí sale que la ecuación de z(t) sea igual a la de x(t).

# La posición de la partícula en función del tiempo 't' viene dada por el siguiente vector:
# r(t) = (x(t),y(t),z(t))

# ! Aclaración
# En el modelo pedido, la única fuerza que actúa es P = m*g. No hay rozamiento, viento ni curvatura terrestre.
# Por la segunda ley de Newton: F = m*a -> m*g = m*a.
# Al cancelar m, nos queda a = g. Por ende, la masa m de la partícula no influye en absoluto para la trayectoria de la misma.

# Datos de entrada:
# - Posiciones iniciales (x0, y0, z0)
# - Velocidades iniciales (vx0, vy0, vz0) 
# - Instante futuro donde se quiere obtener la posición.
# Definimos la gravedad, que es la de la Tierra.
g = 9.8

# Salida del programa:
# - Vector posición r

# Ejemplo de uso:
# xt, yt, zt = posicion_t(1, 2, 3, 4, 5, 6, 7), donde:
# - x0 = 1
# - y0 = 2
# - z0 = 3
# - vx0 = 4
# - vy0 = 5
# - vz0 = 6
# - t = 7

def posicion_t(x0, y0, z0, vx0, vy0, vz0, t):
  """
  Calcula la posición (x, y, z) de la partícula en un instante t.
  Usamos esta función para implementar el modelo:
  r(t) = r0 + v0*t + 1/2*a*t^2, con a = (0, -g, 0)
  """
  
  x = x0 + vx0 * t
  y = y0 + vy0 * t - 0.5 * g * t**2
  z = z0 + vz0 * t
  
  return x, y, z

def trayectoria(x0, y0, z0, vx0, vy0, vz0, t_final, n=200):
  """
  Genera n puntos de la trayectoria desde t = 0 hasta t = t_final.
  Devuelve arrays numpy: (xs, ys, zs, ts)
  Ejemplo de uso:
  xs, ys, zs, ts = trayectoria(1, 2, 3, 4, 5, 6, 7)
  """

  ts = np.linspace(0, t_final, n)
  xs, ys, zs = posicion_t(x0, y0, z0, vx0, vy0, vz0, ts)

  return xs, ys, zs, ts

def grafica_trayectoria(xs, ys, zs):
  """
  Grafica la trayectoria 3D usando matplotlib.
  """

  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  ax.plot(xs, ys, zs, label="Trayectoria")
  ax.scatter(xs[0], ys[0], zs[0], color="green", label="Inicio")
  ax.scatter(xs[-1], ys[-1], zs[-1], color="red", label="Final")

  ax.set_xlabel("X")
  ax.set_ylabel("Y")
  ax.set_zlabel("Z")
  ax.legend()

  try:
    ax.set_box_aspect([1, 1, 1])
  except AttributeError:
    pass
  
  try:
    plt.show()
  except Exception:
    plt.savefig("trayectoria.png")
    print("Entorno sin interfaz gráfica → Imagen guardada como trayectoria.png")

def main():
  print("Bienvenido/a al programa para calcular la trayectoria de un tiro parabólico en 3D\n")

  # --- Entrada de datos ---
  print("Por favor ingrese los datos iniciales:\n")

  # Tiempo final
  try:
    tiempoT = float(input("Tiempo final t (en segundos): "))

    if tiempoT < 0:
      print("Error: el tiempo debe ser mayor o igual a 0.")
      return

    # Posiciones iniciales
    x0 = float(input("Posición inicial x0 (m): "))
    y0 = float(input("Posición inicial y0 (m): "))
    z0 = float(input("Posición inicial z0 (m): "))

    # Velocidades iniciales
    vx0 = float(input("Velocidad inicial vx0 (m/s): "))
    vy0 = float(input("Velocidad inicial vy0 (m/s): "))
    vz0 = float(input("Velocidad inicial vz0 (m/s): "))
  except ValueError:
    print("Error: Por favor ingrese solo números válidos.")
    return

  print("\nCalculando la posición en el instante t (s)...")

  # --- Cálculo puntual ---
  xt, yt, zt = posicion_t(x0, y0, z0, vx0, vy0, vz0, tiempoT)

  print(f"\nPosición de la partícula en t = {tiempoT} s:")
  # El comando .4f es para redondear a 4 cifras decimales
  print(f"x(t) = {xt: .4f} m")
  print(f"y(t) = {yt: .4f} m")
  print(f"z(t) = {zt: .4f} m")

  # --- Generación de la trayectoria ---
  print("\nGenerando la trayectoria completa desde t = 0 hasta t =", tiempoT)
  xs, ys, zs, ts = trayectoria(x0, y0, z0, vx0, vy0, vz0, tiempoT)

  # --- Gráfico ---
  print("\nMostrando la trayectoria...")
  grafica_trayectoria(xs, ys, zs)

  print("\nPrograma finalizado correctamente.")

if __name__ == "__main__":
  main()

# ! Aclaración importante
# El trabajo se pensó como si el objeto se lanzara en un espacio donde no hay un "techo" o un "piso". Es decir, el objeto se puede lanzar desde tan alto como se quiera, y puede caer tan bajo como quiera (en el tiempo dado). Por ese motivo hay pruebas en las que la posición en el eje y da negativa.