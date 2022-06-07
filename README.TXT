#Compilador hecho en python

Ejemplo de entrada:
E -> E + T
E -> T
T -> T * F
T -> F
F -> ( E )
F -> id

D -> T id L ;
L -> , id L
L -> @
T -> float
T -> int

S -> S ; S
S -> id := E
S -> print ( L )
E -> id
E -> num
E -> E + E
E -> ( S , E )
L -> E
L -> L , E

