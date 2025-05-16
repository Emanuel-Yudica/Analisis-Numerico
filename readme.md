
# Análisis Numérico - Propagación del error en la evaluación de funciones
## Emanuel Yudica y Franco Zapata
Este proyecto permite ingresar una función con n variables, calcular su valor en un punto y estimar el error por derivadas parciales usando `SymPy`.

---

## 📦 Requisitos

- Python 3.8 o superior

- pip (ya viene con Python)

---

## ⚙️ Instalación

### 🔵 En Windows
` python -m pip install ` 

` python -m venv venv `

` venv\Scripts\activate `

` pip install -r requirements.txt `

` python main.py `

## En Linux o MacOS
` python3 -m venv venv `

` source venv/bin/activate `

` pip install -r requirements.txt `

` python main.py `

---

## Sobre el uso

- 1.  Ejecuta el script.
- 2.  Se mostrará un ejemplo de sintaxis para ingresar la función.
- 3.  Ingresa la función matemática que deseas evaluar, utilizando letras para las variables (por ejemplo, `x`, `y`, `z`).
- 4.  El programa te pedirá el valor y la cota para cada variable presente en tu función. En caso de no conocerla, dejar el campo en blanco. Se considerará que la cota es igual a la mitad del decimal próximo del valor asignado.
- 5.  Finalmente, se mostrará el valor de la función en el punto dado, las derivadas parciales y los errores absoluto, relativo y porcentual estimados.

---
