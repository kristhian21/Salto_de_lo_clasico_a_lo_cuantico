# Simulador de experimentos

_Esta libreria sirve para realizar los siguientes experimentos de sistemas dinamicos:_

- Experimento de las canicas con coeficiente booleanos
- Experimento de las múltiples rendijas clásico probabilístico, con más de dos rendijas
- Experimento de las múltiples rendijas cuántico

_Adicionalmente la libreria cuenta con una funcion "graficarEstados()" que permite graficar el vector de estados resultante de los experimentos_

## Funcionamiento

_Para usar esta libreria es necesario tener Python instalado y descargar esta libreria_

## Entradas

_Para el experimento de las canicas y el experimento de las rendijas probabilistico las entradas son numeros reales_

_ejemplo:_

- Matriz_adyacencia = [[1, 0, 1],
                       [1, 1, 0],
                       [0, 0, 1]]
                       
- Vector_estados = [1, 0, 1]

_Para el experimento de las rendijas cuantico las entradas son numeros imaginarios que estan representados como un tupla:_

- numeroImaginario: (parteReal, parteImaginaria)
