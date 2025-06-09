# Instalación: Distribución, entornos de desarrollo y sistema de control de versiones

## Fácil: Google Colab

La manera más fácil de trabajar con Python mediante notebooks es emplear [Google Colab](https://colab.research.google.com/).

![Google Colab](Recursos/Google_Colab1.png)

Google Colab permite cargar y correr todos los Notebooks del curso sin preocuparse por las dependencias, entornos de desarrollo o del sistema de control de versiones. Para más de uno será la manera ideal de trabajar. Solo necesitas una cuenta de Google.

Existen diversas maneras de correr los Notebooks, aquí solo veremos la forma larga:

![Google Colab](Recursos/Google_Colab_Github.png)

Simplemente ve al menú **Archivo** y selecciona la opción **Abrir Notebook**, y abre la pestaña **Github**. Saldrá la ventana que se muestra en la imagen anterior. Solo agrega la dirección del repositorio en Github, Google Colab detectará todos los notebooks en el repositorio y podrás cargarlos con un par de clics.

**Actividad**

Carguen el repositorio de este curso.

## Difícil: Instalación completa

Esta es una pequeña guía de instalación de Python (Conda), git, y VS Code para los sistemas operativos Windows y distribuciones Linux (Ubuntu o basadas en Ubuntu, como Linux  Mint).

## Conda

Este curso emplea la distribución y entornos de desarrollo de [Conda](https://www.anaconda.com/download/success). 

Existen dos versiones del instalador: Anaconda y Miniconda. La diferencia principal entre ambos es que Anaconda incluye por default un entorno base más completo además de una interfaz gráfica que provoca que el instalador pese alrededor de 1GB, mientras que Miniconda solo tiene un entorno base básico que solo permite crear y administrar nuevos entornos, por lo cual pesa apenas unos 90MB. Por conveniencia y por motivos didácticos, descargaremos la versión Miniconda, señalada con el siguiente texto:

![Miniconda](Recursos/C0_Instalador_Miniconda.jpg)

### Para Windows

1. Descargar el instalador gráfico 

![Instalador Conda de Windows](Recursos/C0_Instalador_Windows.jpg)

2. Una vez descargado, se ejecuta el instalador.

3. Al preguntar para que usuarios debe instalarse, dejar activado "Just me" como se ve en la imagen

![Usuarios de Miniconda](Recursos/C0_Instalacion_Windows_usuarios.jpg)

4. Al preguntar la ruta de instalación, es recomendable dejar la ruta default como se ve en la imagen. 

![Ruta de Instalación de Miniconda](Recursos/C0_Instalacion_Windows_ruta.jpg)

Si tu nombre de usuario contiene un espacio, como por ejemplo "Antonio Rivera", es recomendable entonces cambiar la ruta de instalación como se muestra en las imágenes usando la opción "Browse..."

![Ruta de Instalación de Miniconda Fix1](Recursos/C0_Instalacion_Windows_ruta_fix01.jpg)

![Ruta de Instalación de Miniconda Fix1](Recursos/C0_Instalacion_Windows_ruta_fix02.jpg)

5. Al llegar a esta ventana, activar todas las opciones. 

![Opciones de Instalación de Miniconda](Recursos/C0_Instalacion_Windows_01.jpg)

Estas opciones son importante por las siguientes razones:
* La primera opción crea el acceso directo en el menu de inicio de Windows a el cmd y el Powershell que inician conda.
* La segunda opción permite que VS Code y otros editores detecten automáticamente los entornos de desarrollo que vamos a crear. Si la advertencia causa mucho "ruido", puede desactivarse pero iniciar los entornos de conda requiere hacerse manualmente. Esta opción es útil si se tiene otro software, como Blender, que necesite su propia versión de Python.
* Detecta la versión del entorno base como la default del sistema.
* La cuarta opción libera el cache después de la instalación, muy útil si se esta experimentando y se reinstala Miniconda o Anaconda varias veces por cualquier razón.

6. Continuar y dejar que la instalación termine, cerrar la ventana de instalación desactivando las opciones finales que solo son un pequeño tour de conda.

![Fin de Instalación de Miniconda](Recursos/C0_Instalacion_Windows_fin.jpg)

7. Para comprobar que todo este en orden, iniciar el Powershell de conda desde el menú de inicio

![Conda en el inicio de Windows 10](Recursos/C0_Inicio_Windows.jpg)

8. Checar que en efecto todo este correcto ejecutando Python en este Powershell y corriendo alguna línea sencilla

![Prueba de Conda en Windows 10](Recursos/C0_Prueba_Windows.jpg)

### Para distribuciones Linux

1. Descargar el instalador de línea de comandos (el primero para la gran mayoría de usuarios) ![Instalador Conda de Distribuciones Linux](Recursos/C0_Instalador_Linux.jpg)

2. Al terminar de descargar, abrir un terminal en la ruta donde está el archivo y ejecutar

```bash
bash ./<nombre_del_archivo>.sh
```

donde

```bash
<nombre_del_archivo>
```

es el nombre correspondiente que tenga el instalador.

3. Una vez ejecutandose el instalador, mantener oprimido *enter* hasta que te pregunte si quieres instalar el software, escribe *yes*.

4. Te preguntará donde quieres realizar tu instalación y ofrece una ruta default, para la mayoría de los casos la ruta default funciona perfectamente, así que solo oprime *enter*

5. Te preguntará si quieres inicializar conda con la terminal, esto principalmente agrega conda al *PATH* y permite detectar automáticamente los entornos que se vayan creando en VSCode, así que escribe *yes*.

6. Al finalizar, no salgas inmediatamente al salir, conda desplagará un comando que es importe. Este comando es:

```bash
conda config --set auto_activate_base false
```

simplemente copialo (o copia este mismo) y cierra la terminal.

7. Vuelve a abrir la terminal, pega el comando y ejecutalo. Vuelve a cerrar la terminal.

8. Si lo hiciste correctamente, ahora al abrir terminal y ejecutar el comando

```bash
conda activate
```

podrás inicializar el entorno base que viene con tu instalación y podrás empezar a crear y administrar entornos de desarrollo.

## Git

[Git](https://git-scm.com/downloads) es el software de control de versiones de proyectos más comúnmente empleado, con una gran compatibilidad de software de terceros que van desde los repositorios en línea como GitHub, GitLab y Azure, y editores de texto como VS Code o PyCharm. 

Veremos como instalarlo tanto para Windows como distribuciones Linux

### Para Windows

1. Descargar el instalador (de 64 bits para la mayoría de los usuarios) del link [Git Descarga](https://git-scm.com/downloads/win)

![Instalador git de Windows](Recursos/C0_git_Windows.jpg)

2. Una vez descargado se ejecuta el instalador

3. Al preguntar por la ruta de instalación, dejar la default

![Ruta del instalador git de Windows](Recursos/C0_git_Windows_instalacion_ruta.jpg)

4. Al preguntar por los componentes, activar la penúltima y antepenúltima opción

![Componentes del instalador git de Windows](Recursos/C0_git_Windows_instalacion_componentes.jpg)

5. A continuación hay una serie de pantallas con varias opciones a escoger, aquí es importante dejar seleccionadas **TODAS** las opciones default. Se dejan las capturas de pantalla con estas opciones para revisar y corregir en caso de algún accidente

![Opciones del instalador git de Windows](Recursos/C0_git_Windows_instalacion_opciones01.jpg)

![Opciones del instalador git de Windows](Recursos/C0_git_Windows_instalacion_opciones02.jpg)

![Opciones del instalador git de Windows](Recursos/C0_git_Windows_instalacion_opciones03.jpg)

![Opciones del instalador git de Windows](Recursos/C0_git_Windows_instalacion_opciones04.jpg)

![Opciones del instalador git de Windows](Recursos/C0_git_Windows_instalacion_opciones05.jpg)

![Opciones del instalador git de Windows](Recursos/C0_git_Windows_instalacion_opciones06.jpg)

![Opciones del instalador git de Windows](Recursos/C0_git_Windows_instalacion_opciones07.jpg)

![Opciones del instalador git de Windows](Recursos/C0_git_Windows_instalacion_opciones08.jpg)

![Opciones del instalador git de Windows](Recursos/C0_git_Windows_instalacion_opciones09.jpg)

![Opciones del instalador git de Windows](Recursos/C0_git_Windows_instalacion_opciones10.jpg)

![Opciones del instalador git de Windows](Recursos/C0_git_Windows_instalacion_opciones11.jpg)

6. Al terminar, simplemente dejar que se complete la instalación y salir

![Fin del instalador git de Windows](Recursos/C0_git_Windows_instalacion_fin.jpg)

### Para Linux

El proceso en Linux (para distribuciones basadas en Ubuntu/Debian) es muy sencillo, simplemente ir a la terminal y ejecutar

```bash
sudo apt install git
```

## Visual Studio Code o VS Code 

**No confundir con Visual Studio, ese es otro software**

[Visual Studio Code](https://code.visualstudio.com/) es un editor de textos , de código libre (en el 99% de todos sus componentes) y probablemente el más utilizado en la industria actualmente. Su fortaleza y popularidad radica principalmente en su fácil empleo, su amplia extensibilidad y configuración, y el como integra las herramientas de software como son el control de versiones (git), detección automática de entornos de desarrollo (conda, pipenv), así como debuggers y unit testers.

A continuación veremos su proceso de instalación.

### Para Windows

1. Descargamos VS Code para Windows 

![Descarga VS Code de Windows](Recursos/C0_vscode_Windows_descarga.jpg)

2. Ejecutamos el instalador

3. Damos la ruta de instalación como se ve en la imagen

![Ruta de instalación VS Code de Windows](Recursos/C0_vscode_Windows_ruta.jpg)

4. Cuando lo pregunte, seleccionamos las siguientes opciones

![Opciones de instalación VS Code de Windows](Recursos/C0_vscode_Windows_opciones.jpg)

5. Terminar la instalación

### Para Linux

1. Descargamos VS Code para la distribución Linux que estés usando: para basadas en Ubuntu/Debian, el archivo .deb; para basadas en Fedora/Red Hat, el archivo .rpm.

![Descarga VS Code de Windows](Recursos/C0_vscode_Linux_descarga.png)

2a. Si tu distribución ya tiene un instalador gráfico de paquetes, simplemente hacer clic e instalar.

2b. Si tu distribución no tiene un instalador gráfico de paquetes, seguir las instrucciones según tu distribución de la página oficial [Instrucciones para instalación en Linux](https://code.visualstudio.com/docs/setup/linux#_install-vs-code-on-linux)

__________________________________________________________

Con estas tres piezas de software correctamente instaladas en el equipo, ya es momento de empezar a trabajar en nuestro **flujo de trabajo**.

## Creando entornos de desarrollo con Conda

### ¿Qué es un entorno de desarrollo?

Python, así como muchos otros lenguajes de programación, cuenta con un universo de bibliotecas y paqueterías que ayudan al desarrollo de software ya que evita que el desarrollador deba "reinventar la rueda" cada que se encuentra con un problema que ya ha sido resuelto antes. 

La solución inmediata que ofrece el lenguaje es instalar estas paqueterías empleando **pip**, sin embargo, algo que no dicen (o que llegamos a ignorar) es que si se hacen estas instalaciones mediante el flujo de trabajo usual, que es instalar Python y luego instalar las paqueterías con pip, es que se instala en el *entorno global*, es decir, que afectan a todo nuestro equipo. Esto no es un problema si solo se instalan pocas paqueterías pero al ir trabajando en diversos proyectos, estos requieren que se instalen una gran y diversa cantidad de paqueterías, muchas veces conflictuando entre si, y ocasionando serios desastres en un futuro que es más cercano de lo que se puede imaginar.

Para evitar estos problemas, se crearon los **entornos de desarrollo virtuales**. Para entender fácilmente lo que es un entorno de desarrollo virtual, imagina lo siguiente: 

Tienes un taller (tu equipo) donde solo puedes tener una version por cada herramienta que uses, este tu entorno de desarrollo global; un día te llega un nuevo trabajo que requiere un martillo diferente al que usualmente usas, como no puedes tener dos martillos en el taller y no puedes deshacerte del viejo martillo porque lo usas para otros trabajos más frecuentes (como pueden ser tareas usuales que realiza tu sistema operativo), optas por crear un entorno de trabajo virtual, que en este caso puedes considerarlo como una caja de herramientas aislada del resto del taller y que solo se abre (activa) cuando te dedicas a este trabajo en específico. De este modo, puedes tener los dos martillos sin ningún tipo de problema o conflicto. 

Así, los entornos de desarrollo pueden virtuales pueden considerarse como cajas de herramientas armadas para un trabajo en concreto y que solo se activan cuando es necesario.

### Además de Conda, ¿Qué alternativas se tienen y cual usar?

Existen varios creadores y administradores de entornos de desarrollo para Python. En este curso nos vamos a enfocar en Conda pero existen otros como [Pipenv](https://pipenv.pypa.io/en/latest/) y [Poetry](https://python-poetry.org/). ¿Cuál es el mejor o cuál debería usar? La respuesta es muy sencilla: el que más te agrade (o le agrade a tu equipo de proyecto) para proyectos nuevos y en el caso de proyectos que ya llevan tiempo en desarrollo, el que se esté usando. 

Hace algunos años Conda ofrecía ciertas ventajas sobre los demás pero conforme estos administradores han ido mejorando, realmente no hay diferencia significativa para Python, la única diferencia actual que todavía es considerable es que Conda puede crear entornos que incluya paquetería de lenguajes que no son Python, tal es el caso de R, C/C++ y FORTRAN. Con esto, si llega algún proyecto que requiera incluir otros lenguajes, Conda es buena opción.

### ¿Cómo creo y administro entornos de desarrollo para Python empleando Conda?

**Para Windows usaremos Anaconda Prompt Powershell, para distribuciones Linux se emplea la Terminal**

Para la administración básica de entornos de desarrollo solo se necesitan dos comandos:

```bash
conda create -n <nombre> <paquete1> <paquete2> <paquete3>
```

y

```bash
conda remove -n <nombre> --all
```

El primero permite crear los enternos de desarrollo y el segundo eliminarlos completamente.

El comando

```bash
-n <nombre>
```

es para declarar el nombre del entorno, asi que por ejemplo, puede quedar 

```bash
-n mi_entorno
```

### ¿Qué hay de Github Desktop?

Github Desktop es una alternativa gráfica ppara emplear git y administrar tus repositorios Github.

[Github Desktop](hhttps://desktop.github.com/download/)

**Actividad** 

Realiza la instalación completa de Conda, git y VSCode en tu equipo.