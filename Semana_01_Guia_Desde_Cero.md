# Semana 1 — Guía desde cero absoluto

Esta guía asume que nunca programaste y que nunca usaste una consola. Cada paso dice qué hacer, qué vas a ver en pantalla, y qué hacer si algo sale distinto. Se sigue en orden, sin saltar.

Horario de referencia (ajustalo a tu vida, respetá los bloques):
08:00–08:30 repaso · 08:30–10:30 teoría · 10:45–12:30 práctica · 13:30–16:00 proyecto · 16:00–16:30 diario y cierre.
El lunes no hay nada que repasar todavía: arrancás 8:00 directo con el Paso 1.

---

## DÍA 1 (LUNES) — La terminal, Python y tu primer programa

### Parte A — Entender qué vas a hacer (30 min, solo lectura)

**¿Qué es programar?** Escribir instrucciones exactas, en un lenguaje que la computadora entiende, para que haga algo por vos. La computadora es obediente y tonta: hace exactamente lo que escribiste, no lo que quisiste decir. El 80% de aprender a programar es acostumbrarse a esa exactitud.

**¿Qué es Python?** Uno de esos lenguajes. Elegimos Python porque se lee casi como inglés y porque es el lenguaje estándar de la automatización y la IA — el que piden los trabajos a los que apuntamos.

**¿Qué es la terminal (o consola)?** Una ventana donde le das órdenes a la computadora escribiendo texto, en vez de hacer clic en íconos. Todo lo que hacés con el mouse tiene un equivalente escrito, y los desarrolladores usan la versión escrita porque es más rápida, más precisa y se puede automatizar. En Windows la terminal moderna se llama **PowerShell**.

### Parte B — Abrir PowerShell por primera vez (15 min)

1. Apretá la tecla **Windows** (la del logo, abajo a la izquierda del teclado).
2. Escribí: `powershell` (mientras escribís, Windows busca).
3. Apretá **Enter**.

Se abre una ventana con fondo azul o negro que muestra algo como:

```
PS C:\Users\TuUsuario>
```

Eso se llama **prompt**. Significa: "estoy lista, dame una orden". La parte `C:\Users\TuUsuario` te dice **en qué carpeta estás parado** — la terminal siempre está "parada" en alguna carpeta, igual que el Explorador de Windows siempre muestra alguna carpeta.

**Tus primeras cuatro órdenes.** Escribí cada una y apretá Enter. Observá qué pasa antes de seguir con la siguiente:

```
pwd
```
Te muestra la carpeta donde estás (print working directory). Debe coincidir con lo que dice el prompt.

```
dir
```
Lista lo que hay dentro de la carpeta actual (directorio). Vas a reconocer tus carpetas: Documents, Downloads, etc.

```
cd C:\Dev
```
Te mueve a la carpeta C:\Dev (change directory). El prompt ahora dice `PS C:\Dev>`.

```
dir
```
Otra vez, pero ahora estando en C:\Dev. Vas a ver la carpeta `entrenamiento`, que es donde está esta guía.

**Si escribís mal una orden**, la terminal te lo dice con un mensaje rojo y no pasa nada malo. Leé el mensaje — leer errores completos, sin miedo, es un hábito profesional que empieza hoy.

### Parte C — Instalar Python (45 min)

1. Abrí el navegador y andá a **python.org** → botón **Downloads** → descargá la última versión para Windows (3.12 o superior).
2. Ejecutá el instalador descargado.
3. **PASO CRÍTICO — leé antes de hacer clic:** en la primera pantalla del instalador hay una casilla abajo que dice **"Add python.exe to PATH"**. **MARCALA.** Si no la marcás, Windows no va a saber dónde quedó Python y la terminal no lo va a encontrar. Es el error #1 de todo principiante.
4. Clic en "Install Now" y esperá.
5. Cuando termine, **cerrá la ventana de PowerShell y abrí una nueva** (las terminales leen la configuración al abrirse; la vieja no se entera de que Python existe).
6. En la PowerShell nueva escribí:

```
python --version
```

Si responde algo como `Python 3.12.4`, Python está instalado y funcionando. 

**Si responde "python no se reconoce como comando":** la casilla de PATH no quedó marcada. Solución: volvé a ejecutar el instalador → "Modify" → siguiente → en "Advanced Options" marcá "Add Python to environment variables" → Install. Cerrá y abrí PowerShell de nuevo y repetí la prueba.

### Parte D — Instalar Visual Studio Code (30 min)

VS Code es el **editor** donde vas a escribir código. La terminal ejecuta; el editor escribe. Son las dos herramientas de tu oficio nuevo.

1. Andá a **code.visualstudio.com** y descargá para Windows. Instalá con las opciones por defecto (podés marcar "Add 'Open with Code' action" — es útil).
2. Abrí VS Code.
3. Menú **File → Open Folder** → navegá a `C:\Dev\entrenamiento` → Select Folder. Si pregunta si confiás en los autores, decí que sí (los autores sos vos).
4. A la izquierda ves el **explorador de archivos** de la carpeta. Ahí están esta guía y el plan.
5. Instalá la extensión de Python: a la izquierda hay un ícono de bloques (Extensions), clic, buscá "Python", instalá la de Microsoft.
6. Truco que une todo: menú **Terminal → New Terminal**. Se abre una PowerShell *adentro* de VS Code, ya parada en tu carpeta. Vas a trabajar así: código arriba, terminal abajo.

### Parte E — Tu primer programa (después del almuerzo)

1. En VS Code, con la carpeta abierta, clic derecho en el explorador → **New Folder** → llamala `semana01`.
2. Clic derecho sobre `semana01` → **New File** → llamalo `hola.py` (la extensión `.py` le dice al mundo que es un archivo de Python).
3. Adentro escribí exactamente esto (vos, tecla por tecla — regla 1):

```python
print("Hola, soy Ricardo y estoy aprendiendo Python")
```

4. Guardá con **Ctrl+S**. (Guardar compulsivamente es otro hábito del oficio: el punto blanco en la pestaña significa "sin guardar".)
5. En la terminal de VS Code escribí:

```
cd semana01
python hola.py
```

Si la pantalla dice tu frase: **acabás de ejecutar tu primer programa.** No es simbólico — el mecanismo que acabás de usar (escribir instrucciones en un archivo, pedirle a Python que las ejecute) es exactamente el mismo con el que funcionan los sistemas de un millón de líneas.

6. Experimentá 30 minutos: cambiá el texto, agregá más líneas de `print`, rompelo a propósito (borrá una comilla, guardá, ejecutá) y **leé el mensaje de error completo**. Los errores de Python te dicen archivo, línea y tipo de problema — son un GPS, no un regaño.

### Parte F — Variables, tu primera herramienta real (resto de la tarde)

Creá un archivo nuevo `variables.py` y escribí, ejecutando después de cada bloque para ver qué hace:

```python
# Esto es un comentario: Python lo ignora, es una nota para humanos
nombre = "Ricardo"
edad = 40
print(nombre)
print(edad)
```

Una **variable** es una caja con etiqueta: guardás un valor adentro y lo usás por su nombre. Probá:

```python
proyecto = "Eva"
anios_experiencia = 14
mensaje = "Trabajando en " + proyecto
print(mensaje)
print(anios_experiencia + 10)
```

Fijate en dos cosas: los textos van entre comillas (se llaman *strings*), los números no. Y el `+` hace cosas distintas según el tipo: junta textos, suma números. Probá qué pasa con `print(nombre + edad)` — va a fallar. Leé el error: te está diciendo que no puede juntar un string con un número. Ese tipo de lectura de errores es la habilidad del día.

**Ejercicios del día (en un archivo `ejercicios_dia1.py`):**
1. Creá variables con tu nombre, ciudad, y año de nacimiento, e imprimí una presentación usando las tres.
2. Calculá e imprimí cuántos años vas a tener en 2030 usando la variable del año de nacimiento.
3. Creá una variable `tarifa_hora = 16` y otra `horas_semana = 40` e imprimí cuánto es por semana y por mes (4 semanas).

### Parte G — Cierre del día (16:00–16:30)

1. En la carpeta `diario`, copiá la plantilla (`plantilla_diario.md`) a un archivo nuevo llamado `2026-08-10.md` (en VS Code: clic derecho sobre la plantilla → Copy, clic derecho en la carpeta → Paste, renombrá).
2. Respondé las tres preguntas del diario. En serio, por escrito. Es la regla 4.
3. Cerrá todo. No estudies de noche esta semana: el sueño es parte del método.

---

## DÍA 2 (MARTES) — Decisiones: los condicionales

**08:00–08:30 Repaso:** releé tu diario de ayer. Después, sin mirar los archivos de ayer, escribí de memoria en un archivo nuevo `repaso.py`: una variable de texto, una de número, y un print que las combine. Si no te sale de memoria, está bien — miralo, cerralo, intentalo de nuevo. Eso ES el repaso activo.

**Teoría (08:30–10:30):** los programas toman decisiones con `if` (si), `elif` (si no, y si...) y `else` (si no, entonces). Escribí y ejecutá:

```python
tarifa = 45

if tarifa > 40:
    print("Tarifa de arquitecto")
elif tarifa > 20:
    print("Tarifa intermedia")
else:
    print("Tarifa de entrada")
```

Dos reglas de oro de Python que ves aquí:
- Los dos puntos `:` al final de la línea del `if` son obligatorios.
- Las líneas de adentro van **indentadas** (corridas 4 espacios). En Python la indentación no es estética: define qué está "adentro" de qué. La tecla Tab en VS Code lo hace por vos.

Probá los operadores de comparación uno por uno: `>` `<` `>=` `<=` `==` (igual — ojo: doble igual, porque el simple ya se usa para asignar variables) y `!=` (distinto). Y los conectores `and`, `or`, `not`.

**Práctica (10:45–12:30), archivo `ejercicios_dia2.py`:**
1. Un programa con una variable `puntaje_gate = 0.71` y un umbral `0.75`: imprimir "PASS" si el puntaje es mayor o igual al umbral, "FAIL" si no. (Sí: es tu compuerta de Eva, versión de juguete. Todo el entrenamiento va hacia ahí.)
2. Ampliarlo: si el puntaje está a menos de 0.05 del umbral, imprimir "FAIL — cerca del umbral, reintentar"; si está más lejos, "FAIL — revisar configuración".
3. Un clasificador de tarifas de Upwork: variable `tarifa`, imprimir la banda ("menos de 20", "20 a 40", "más de 40") usando if/elif/else.
4. Un verificador de conexión: variables `payment_verified = True` y `total_gastado = 143`; imprimir "aplicar" solo si el pago está verificado Y el gasto es mayor a 1000, si no "no aplicar". (True/False se llaman *booleanos* — investigá 10 minutos qué son antes de hacerlo.)

**Proyecto (13:30–16:00):** el programa `decidir_aplicacion.py`: combiná todo lo anterior en un solo programa que, dadas 4 variables de un anuncio de Upwork (tarifa, pago verificado, gasto total del cliente, horas semanales), imprima una recomendación razonada con varios prints. Probalo cambiando los valores a mano y verificando que cada rama funciona — probar cada rama es tu primer acto de QA sobre tu propio código.

**Cierre:** diario `2026-08-11.md`. Tres preguntas.

---

## DÍA 3 (MIÉRCOLES) — Repetición: los bucles

**Repaso (08:00):** de memoria, escribí un if/elif/else que clasifique un número en negativo/cero/positivo. Después corregite mirando los archivos de ayer.

**Teoría (08:30–10:30):** dos formas de repetir:

```python
# for: repetir para cada elemento de una serie
for numero in range(5):
    print("Iteración número", numero)

# while: repetir mientras una condición sea cierta
intentos = 0
while intentos < 3:
    print("Reintento", intentos)
    intentos = intentos + 1
```

Cosas para descubrir experimentando (30 min mínimo): ¿desde qué número empieza `range(5)` y en cuál termina? ¿Qué pasa si el `while` nunca deja de ser cierto? (Spoiler: bucle infinito — se corta con **Ctrl+C** en la terminal. Hacelo a propósito una vez para perderle el miedo.)

**Práctica (10:45–12:30), `ejercicios_dia3.py`:**
1. Imprimir los números del 1 al 20, pero al lado de cada múltiplo de 5 agregar la palabra "checkpoint".
2. Sumar todos los números del 1 al 100 usando un for y una variable acumuladora (empezá con `total = 0`).
3. Simular reintentos: un `while` que "intente" hasta 3 veces y después imprima "ESCALATE — límite de reintentos alcanzado". (Tu escalation bridge, versión día 3.)
4. Tabla de conversión: para cada tarifa en `range(10, 55, 5)` imprimir la tarifa y cuánto queda después del 10% de comisión de Upwork.

**Proyecto (13:30–16:00):** `simulador_reintentos.py` — combiná bucle + condicional: una "compuerta" con umbral 0.75 evalúa una lista de puntajes que le das vos a mano (aprendés listas mañana; hoy usá varias variables o un range), cuenta cuántos PASS y cuántos FAIL hubo, e imprime el resumen final. El concepto de *acumular resultados dentro de un bucle* es la mecánica número 1 de todo procesamiento de datos.

**Cierre:** diario.

---

## DÍA 4 (JUEVES) — Funciones: darle nombre a las cosas

**Repaso (08:00):** de memoria: un for que sume los números del 1 al 10.

**Teoría (08:30–10:30):** una **función** es un bloque de código con nombre, que recibe datos y devuelve un resultado. Es el concepto más importante de la semana:

```python
def evaluar_gate(puntaje, umbral):
    if puntaje >= umbral:
        return "PASS"
    else:
        return "FAIL"

resultado = evaluar_gate(0.71, 0.75)
print(resultado)
```

Fijate: `def` la define, los paréntesis reciben los datos (parámetros), `return` devuelve el resultado. Definir la función no la ejecuta — se ejecuta cuando la *llamás* por su nombre. Llamala varias veces con números distintos: escribiste la lógica una vez, la usás mil veces. Eso es programar.

**Práctica (10:45–12:30), `ejercicios_dia4.py`:**
1. Función `neto_upwork(tarifa)` que devuelva la tarifa menos el 10%.
2. Función `clasificar_cliente(pago_verificado, gasto_total)` que devuelva "aplicar" o "no aplicar".
3. Función `veredicto(puntaje, umbral)` que devuelva "PASS", "FAIL — cerca" (a menos de 0.05) o "FAIL — lejos".
4. Reescribí el proyecto de ayer usando funciones: el programa principal queda en 5 líneas que llaman funciones. Sentí la diferencia de claridad — esa sensación es "código organizado" y la vas a perseguir 6 meses.

**Proyecto (13:30–16:00):** `gate_toolkit.py` — tu primera "caja de herramientas": 4–5 funciones relacionadas con evaluar compuertas (evaluar, contar resultados, calcular tasa de aprobación, decidir si escalar), y abajo un bloque principal que las usa en secuencia con datos de prueba. Este archivo es el ancestro directo del `veredicto-cli` del plan maestro.

**Cierre:** diario. Anotá especialmente qué diferencia sentiste entre el código del miércoles y el del jueves.

---

## DÍA 5 (VIERNES) — Repaso, GitHub y Compuerta S1

Sin contenido nuevo de Python. Hoy se consolida y se abre tu vitrina profesional.

**08:00–09:30 Repaso acumulado:** releé los cuatro diarios. Después, con todos los archivos cerrados, escribí de memoria en `repaso_semana.py`: una función que reciba un número y use un if para clasificarlo, llamada desde un bucle for con `range(10)`. Es la semana entera en 10 líneas.

**09:30–11:00 GitHub — tu portafolio nace hoy:**
1. Andá a **github.com** → Sign up. Elegí un nombre de usuario profesional (va a estar en tus propuestas de Upwork; algo como `ricardo-apellido` o similar, no apodos de gaming).
2. Instalá Git desde **git-scm.com** (opciones por defecto en todo el instalador — son muchas pantallas, Next a todo).
3. Cerrá y reabrí VS Code. En la terminal, presentate ante Git (una sola vez en la vida, con tus datos):
```
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email-de-github@ejemplo.com"
```
4. En github.com: botón **New repository** → nombre `training-week01` → Public → Create.
5. GitHub te muestra instrucciones; usamos estas, desde tu terminal parada en `C:\Dev\entrenamiento\semana01`:
```
git init
git add .
git commit -m "Week 1: Python basics - variables, conditionals, loops, functions"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/training-week01.git
git push -u origin main
```
(Te va a pedir iniciar sesión en GitHub la primera vez — seguí el flujo del navegador.)
6. Refrescá la página de tu repo: tu código de la semana está publicado. No entiendas todavía qué hizo cada comando de Git — en la semana 3 lo desarmamos; hoy solo importa que el hábito del commit empiece.

**11:00–12:30 Demo grabada:** 3 minutos, en inglés, con OBS o Loom (instalá el que prefieras): pantalla compartida mostrando `gate_toolkit.py`, ejecutándolo, y explicando qué hace. Va a salir torpe. Perfecto: es la línea base contra la que vas a medir tu progreso en la semana 24.

**13:30–15:00 COMPUERTA S1 (evaluación real, sin ayuda, sin mirar archivos viejos, 90 minutos):**
Abrí un chat conmigo y decime: "Compuerta S1". Te voy a dar 5 ejercicios sorpresa de variables, condicionales, bucles y funciones, calibrados a lo que estudiaste. Criterio de paso: 4 de 5 funcionando. Si pasás → el lunes te entrego la guía de la Semana 2. Si no pasás → el lunes reforzamos juntos lo que falló y la compuerta se repite el martes. Ninguna de las dos cosas es buena o mala noticia: son información, como todos tus gates.

**15:00–16:00 Retrospectiva escrita** (en `diario\retro_semana01.md`): ¿qué costó más de lo esperado? ¿qué costó menos? ¿el horario funcionó o hay que moverlo? ¿cuántas veces rompiste la regla de escribir todo vos? (Sé honesto — es tu programa, mentirte es robarte.)

---

## Errores comunes de la semana 1 (consultá antes de frustrarte)

- **"python no se reconoce..."** → PATH. Ver Día 1 Parte C paso 6.
- **`SyntaxError`** → escribiste algo que Python no puede leer: comilla sin cerrar, falta un `:`, paréntesis sin cerrar. Mirá la línea que señala el error y la anterior.
- **`IndentationError`** → problema de espacios al inicio de línea. Todo lo que está "adentro" de un if/for/def va corrido con Tab, consistentemente.
- **`NameError: name 'x' is not defined`** → usaste una variable antes de crearla, o la escribiste distinto (Python distingue mayúsculas: `Nombre` y `nombre` son variables diferentes).
- **El programa "no hace nada"** → ¿guardaste el archivo antes de ejecutar? (punto blanco en la pestaña = no guardado). ¿Ejecutaste el archivo correcto?
- **Escribo en la terminal y no pasa nada** → ¿apretaste Enter? ¿la terminal está esperando algo de otro comando anterior? (Ctrl+C la libera).
