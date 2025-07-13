estudiantes = {}

cantidad = int(input("¿Cuántos estudiantes vas a registrar? "))

for _ in range(cantidad):
    nombre = input("Nombre del estudiante: ")
    nota = float(input("Nota del estudiante: "))
    estudiantes[nombre] = nota

print("\nResultados:")
for nombre, nota in estudiantes.items():
    estado = "Aprobado" if nota >= 3.0 else "Reprobado"
    print(f"{nombre}: {nota} -> {estado}")
