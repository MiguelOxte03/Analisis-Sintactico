import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = [
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
    # Boolean
    "TRUE",
    "FALSE"]

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
    # Others
    "COMMENTS",
    "COMMENTS_C99",
    "ID",
    "IDVAR",
    "NUM",
    "VOID"
]

# Ignore Characters
t_ignore = "\t"

def t_space(t):
    r"\s+"
    t.lexer.lineno += t.value.count("\n")

def t_VOID(t):
    r"void|VOID"
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print ("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

#  RE SÍMBOLOS
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


# RE OTHERS
def t_COMMENTS(t):
    r"\/\*([^*]|\*[^\/])*(\*)+\/"
    t.lexer.lineno += t.value.count("\n")


def t_COMMENTS_C99(t):
    r"(\/\/|\#)(.)*?\n"
    t.lexer.lineno += 1


def t_IDVAR(t):
    r"\$\w+(\d\w)*"
    return t


# \VAR|var\s\w+(\d\w)*


def t_NUM(t):
    r"\d+(\.\d+)?"
    t.valor = float(t.value)
    return t


def t_ID(t):
    r"\w+(\w\d)*"
    return t


def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t

# RE Tokens
# palabras reservadas
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
    return


def t_RETURN(t):
    r"return"
    return t


def t_MAIN(t):
    r"main"
    return t


def t_VAR(t):
    r"var"
    return
"""
def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

directorio = 'D:/Archivos/Python/AnalizadorSintactico_Dart/Prueba/'
archivo = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()
"""
analizador = lex.lex()
"""
analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok : break
	print (tok)
"""

