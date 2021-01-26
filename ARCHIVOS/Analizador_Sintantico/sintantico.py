import ply.yacc as yacc
from lexico import tokens  # Se importan los toknes del analizador lexico
import re

# Resultado analisis sintactico
resultado_gramatica = []

# Precedencias de los simboles es importanter el orden en el que se declara
precedence = (
    ('right', 'IF', 'ELSE'),
    ('left', 'SEMI'),
    ('left', 'COMMA'),
    ('left', 'EQUAL'),
    ('left', 'SEMI'),
    ('left', 'DEQUAL'),
    ('left', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL', 'ISEQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LBLOCK', 'RBLOCK'),
    ('left', 'LPAREN', 'RPAREN')
)

# Se guarda el mensaje de asignacion
nombres = {}

# Todo que empieza con def es una funcion
# Se definen las condicionales (if)


def p_declaracion_coditionif(t):
    'declaracion : IF LPAREN expresion GREATER expresion RPAREN LBLOCK expresion SEMI RBLOCK'
    t[0] = t[1]  # en dado caso que se quiera reutilizar solo se cambian los tokens con referencia la leguaje

# Declaracion de la instruccion else


def p_declaracion_coditionelse(t):
    'declaracion : ELSE LBLOCK expresion SEMI RBLOCK'
    t[0] = t[1]

# Proceso de asignacion con refencia al tipo de dato
# int


def p_declaracion_asignar(t):
    'declaracion : VAR expresion EQUAL expresion SEMI'
    nombres[t[1]] = t[3]

# Inicio del programa (bloque)


def p_declaracion_inicio(t):
    'declaracion : OPENTAG'
    t[0] = t[1]

# Fin del programa (fin del boque)


def p_declaracion_final(t):
    'declaracion :  CLOSETAG'
    t[0] = t[1]

# Definicion Expresion


def p_declaracion_expr(t):
    'declaracion : expresion SEMI'
    t[0] = t[1]


# Validacion de operandos (+,-,*,/)


def p_expresion_operaciones(t):
    '''
    expresion  :   expresion PLUS expresion
                |   expresion MINUS expresion
                |   expresion TIMES expresion
                |   expresion DIVIDE expresion

    '''
    # Como debe de expresarse las operaciones cuando se este compilando
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]


def p_expresion_operaciones1(t):
    """
    expresion : expresion addop NUM
    | NUM addop expresion
    """
    pass


def p_addop(p):
    """addop : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    """
    pass
# Variante de el menos


def p_expresion_minus(t):
    'expresion : MINUS expresion %prec MINUS'
    t[0] = -t[2]

# Expresiones entre parentesis y corchetes


def p_expresion_grupo(t):
    '''
    expresion  : LPAREN expresion RPAREN
                | LBLOCK expresion RBLOCK
    '''
    t[0] = t[2]

# Expresiones logicas (>,<, =)


def p_expresion_logicas(t):
    '''
    expresion   :  expresion LESS expresion
                |  expresion GREATER expresion
                |  expresion LESSEQUAL expresion
                |   expresion GREATEREQUAL expresion
                |   expresion EQUAL expresion
                |   expresion ISEQUAL expresion
                |  LPAREN expresion LESS expresion RPAREN
                |  LPAREN expresion GREATER expresion RPAREN
                |  LPAREN expresion LESSEQUAL expresion RPAREN
                |  LPAREN expresion GREATEREQUAL expresion RPAREN
                |  LPAREN expresion EQUAL expresion RPAREN
                |  LPAREN expresion ISEQUAL expresion RPAREN
    '''  # Variantes en las expresiones logicas
    if t[2] == "<":
        t[0] = t[1] < t[3]
    elif t[2] == ">":
        t[0] = t[1] > t[3]
    elif t[2] == "<=":
        t[0] = t[1] <= t[3]
    elif t[2] == ">=":
        t[0] = t[1] >= t[3]
    elif t[2] == "==":
        t[0] = t[1] is t[3]
    elif t[2] == "!=":
        t[0] = t[1] != t[3]
    elif t[3] == "<":
        t[0] = t[2] < t[4]
    elif t[2] == ">":
        t[0] = t[2] > t[4]
    elif t[3] == "<=":
        t[0] = t[2] <= t[4]
    elif t[3] == ">=":
        t[0] = t[2] >= t[4]
    elif t[3] == "==":
        t[0] = t[2] is t[4]
    elif t[3] == "!=":
        t[0] = t[2] != t[4]

# Tipos de variables

# Numerica


def p_expresion_num(t):
    'expresion : NUM'
    t[0] = t[1]
# Identificador


def p_expresion_id(t):
    'expresion : ID'
    t[0] = t[1]


# Imprime un tipo de ERROR


def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {:4} en el valor {:4}".format(
            str(t.type), str(t.value))
    else:
        resultado = "Error sintactico {}".format(t)
    resultado_gramatica.append(resultado)


# Analizador sistactico
parser = yacc.yacc()

# funcion que caputa de manera presisa los erroes


def prueba_sintactica(data):
    global resultado_gramatica

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("")
    return resultado_gramatica


# Se lee el archivo de prueba
path = "ejemplo.dart"

# Verificacion y captura de error al buscar el archivo
try:
    archivo = open(path, 'r')
except:
    print("Archivo NO encontrado")
    quit()

text = ""
for linea in archivo:
    text += linea

# Impresion de los resultados
prueba_sintactica(text)
print()
print('************************************************')
print()
print('\n'.join(list(map(''.join, resultado_gramatica))))
