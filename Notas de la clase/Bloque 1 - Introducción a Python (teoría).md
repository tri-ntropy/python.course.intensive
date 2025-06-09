# Introducción a Python

## ¿Qué es Python?
Python es un lenguaje de programación:

* De propósito general
* De *alto nivel*
* Interpretado (principalmente)
* De tipaje fuerte y dinámico
* De multi-paradigma
* Enfocado en la lectura y rápido desarrollo por humanos (pero nada evita que puedas escribir scripts, notebooks, módulos y paqueterías que nadie entienda)
* Es *garbage collected*
* Con *baterías incluídas* y altamente extensible
* Software libre

## Criticismo que ya no es válido desde hace varios años

* *Python es un lenguaje lento (comparado con C o FORTRAN)*. 

Python es lento si se emplea mal. Por lo regular quien argumenta que el lenguaje es lento convenientemente trata de probar su punto creando un ciclo for que itera más de 10000 veces para hacer una simple tarea (como encontrar el máximo en un arreglo/lista de números) y lo compara con C o FORTRAN, ignorando completamente que el ciclo for en Python tiene un comportamiento distinto al resto de lenguajes. Por otra parte, Python ofrece una multitud de herramientas para realizar ese tipo de tareas sin necesidad de un ciclo for, que son virtualmente igual de rápidas en ejecución que C o FORTRAN, pero mucho más rápidas de escribir en Python.

Y hay que ser humildes: Al creador de cierto lenguaje de programación lo criticaron en su momento en su propio espacio de trabajo cuando sus colegas argumentaron que su creación no era útil ya que a nadie le gustaría ver como su proyecto se ejecuta más lento a que si lo escribiera directamente en lenguaje ensamblador o binario. ¿Cuál era este lenguaje? FORTRAN

* *Los espacios en blanco en la sintaxis es mala idea*

Aunque se pueden encontrar situaciones donde los espacios en blanco en efecto pueden crear problemas, esto esta resuelto desde hace varios años gracias a la gran cantidad de editores de texto (y a sus configuraciones) que existen actualmente que permiten manejar sin problema alguno los espacios en blanco en la sintaxis de Python (y otras piezas de código, como lo son los archivos .yaml).

* *Python no te deja pensar*

Gracias al universo de bibliotecas de Python, es muy común encontrar el siguiente chiste

```bash
import solution
```

Lo cual efectivamente, muy frecuentemente es todo o la mayor parte de lo que se necesita para solucionar un problema. Sin embargo, recordemos que en general estamos hablando de programación: si una solución existe (podemos ser filosóficos aquí), es muy probable que existan más soluciones, algunas más rápidas y otras más completas, y dependiendo de la tarea asignada, se puede optar por una o la otra.

Un ejemplo reciente de esto es Deepseek vs ChatGPT hace varios meses (al momento de escribir este archivo markdown). Deepseek, además de implementar sus propios algoritmos, re-implementó el **backend** de manera que optimizó su implementación para que pudiera correr en equipos de bajos recursos, sin embargo, cualquiera que sepa que cambió respecto a otras IAs sabe que no fue algo trivial como simplemente cambiar de lenguaje (Deepseek y ChatGPT ambos emplean Python principalmente)

![Deepseek Python](Recursos/C1_Deepseek_Python.png)

![ChatGPT Python](Recursos/C1_Chatgpt_Python.png)

* *¡Python es un caos!, ¿Cual usar, Python 2.X.X o Python 3.X.X?*

Cuando se lanzó Python 3 hubo demasiados conflictos ya que el lenguaje sufrió una serie de cambios que rompieron la compatibilidad con demasiados proyectos que en ese entonces estaban escritos en Python 2.X.X. Durante años esto generaba fuertes discusiones pero ya no más, desde el primero de enero del año 2020, Python 2.X.X detuvo su desarrollo y prácticamente ningún proyecto serio que siga en desarrollo o mantenimiento usa Python 2.X.X. Ya solo se usa Python 3.X.X.