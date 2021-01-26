import ply.lex as lex

resultado_lexema = []

reservadas = [
    "OPENTAG",
    "CLOSETAG",
    "CASE",
    "CLASS",
    "CONST",
    "PRINT",
    "DO",
    "BREAK",
    "FOR",
    "SWITCH",
    "WHILE",
    "IF",
    "ELSE",
    "STRING",
    "STATIC",
    "RETURN",
    "MAIN",
    "VAR",
    "INT",
    # Boolean
    "TRUE",
    "FALSE",
]

tokens = reservadas + [
    "PLUS",
    "PLUSPLUS",
    "PLUSEQUAL",
    "MINUS",
    "MINUSMINUS",
    "MINUSEQUAL",
    "TIMES",
    "DIVIDE",
    "LESS",
    "LESSEQUAL",
    "GREATER",
    "GREATEREQUAL",
    "EQUAL",
    "DEQUAL",
    "DISTINT",
    "ISEQUAL",
    "SEMI",
    "LPAREN",
    "RPAREN",
    "LBRACKET",
    "RBRACKET",
    "LBLOCK",
    "RBLOCK",
    "COLON",
    "DOT",
    "QUOTES",
    "APOSTROPHE",
    "COMMA",
    # Others
    "COMMENTS",
    "COMMENTS_C99",
    "ID",
    "NUM",
    "VOID",
]

# Ignore Characters
t_ignore = "\t"

"""
def t_space(t):
    r"\s+"
    t.lexer.lineno += t.value.count("\n")
"""


def t_espacio(t):
    r"\s"
    pass


def t_VOID(t):
    r"void|VOID"
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


# RE Tokens
# #  RE SÍMBOLOS
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_EQUAL = r"="
t_DISTINT = r"!"
t_LESS = r"<"
t_GREATER = r">"
t_SEMI = r";"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_LBLOCK = r"{"
t_RBLOCK = r"}"
t_COLON = r":"
t_DOT = r"\."
t_QUOTES = r"\""
t_APOSTROPHE = r"\' "
t_COMMA = r','


def t_LESSEQUAL(t):
    r"<="
    return t


def t_GREATEREQUAL(t):
    r">="
    return t


def t_DEQUAL(t):
    r"!="
    return t


def t_ISEQUAL(t):
    r"=="
    return t


def t_MINUSMINUS(t):
    r"--"
    return t


def t_PLUSPLUS(t):
    r"\+\+"
    return t


# RE OPEN AND CLOSE TAG
def t_OPENTAG(t):
    r"main\s?\(\)\s?\{"
    return t


def t_CLOSETAG(t):
    r"\}"
    return t


# RE OTHERS
def t_COMMENTS(t):
    r"\/\*([^*]|\*[^\/])*(\*)+\/"
    t.lexer.lineno += t.value.count("\n")


def t_COMMENTS_C99(t):
    r"(\/\/|\#)(.)*?\n"
    t.lexer.lineno += 1

# \VAR|var\s\w+(\d\w)*


def t_NUM(t):
    # r'\d+'
    r"\d+(\.\d+)?"
    t.value = float(t.value)
    return t


def t_ID(t):
    r'\w+\=|\w+'
    return t


"""def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t
"""


# palabras reservadas
def t_INT(t):
    r'int|INT'
    return t


def t_CASE(t):
    r"case"
    return t


def t_CLASS(t):
    r"class"
    return t


def t_CONST(t):
    r"conts"
    return t


def t_PRINT(t):
    r"print"
    return t


def t_DO(t):
    r"do"
    return t


def t_FOR(t):
    r"for"
    return t


def t_BREAK(t):
    r"break"
    return t


def t_SWITCH(t):
    r"switch"
    return t


def t_WHILE(t):
    r"while"
    return t


def t_IF(t):
    r"if"
    return t


def t_ELSE(t):
    r"else"
    return t


def t_STATIC(t):
    r"static"
    return t


def t_RETURN(t):
    r"return"
    return t


def t_MAIN(t):
    r"main"
    return t


def t_VAR(t):
    r"var"
    return t


lexer = lex.lex()

# Ingreso


def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Line {:4} Type {:4} >>>>> {:4}".format(
            str(tok.lineno), str(tok.type), str(tok.value))
        resultado_lexema.append(estado)

    return resultado_lexema


# Para abrir archivo
analizador = lex.lex()
path = "ejemplo.dart"

try:
    archivo = open(path, 'r')
except:
    print("Archivo NO encontrado")
    quit()

text = ""
for linea in archivo:
    text += linea
prueba(text)
# Imprimir datos del programa
print('\n'.join(list(map(''.join, resultado_lexema))))
