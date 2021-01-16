import ply.yacc as yacc
import os
import codecs
import re
from lexico import tokens
from sys import stdin

VERBOSE  = 1

precedence = (
    #('right', 'IF'),
    #('left', 'SEMI'),
    ('right', 'EQUAL'),
    ('nonassoc', 'ISEQUAL', 'DEQUAL'),
    ('nonassoc', 'LESS', 'GREATER', 'LESSEQUAL', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LBLOCK', 'RBLOCK'),
    ('left', 'LPAREN', 'RPAREN'),
)

#Estructuras de control
"""
def p_declaracion_coditionif(p):
    '''declaration : IF LPAREN condition relation condition RPAREN LBLOCK condition SEMI RBLOCK'''
    print ("declaracion codition if")

def p_declaration_conditionelse(p):
    '''declaration : ELSE'''
    print ("declaration condition else")

def p_declaration_conditionfor(p):
    '''declaration : FOR'''
    print ("declaration condition for")

def p_declaration_contionwhile(p):
    '''declaration : WHILE'''
    print ("declaration contion while")
"""
#Estructura condicional
def p_condition(p):
    '''condition : expression'''
    print ("condition")

def p_condition1(p):
	'''condition : expression relation expression'''
	print ("condition 1")

def p_relation1(p):
	'''relation : EQUAL'''
	print ("relation 1")

def p_relation2(p):
	'''relation : ISEQUAL'''
	print ("relation 2")

def p_relation3(p):
	'''relation : DEQUAL'''
	print ("relation 3")

def p_relation4(p):
	'''relation : LESS'''
	print ("relation 4")

def p_relation5(p):
	'''relation : GREATER'''
	print ("relation 5")

def p_relation6(p):
	'''relation : LESSEQUAL'''
	print( "relation 6")

def p_relation7(p):
	'''relation : GREATEREQUAL'''
	print ("relation 7")

#Reglas operaciones matematicas
def p_expression1(p):
	'''expression : term'''
	print ("expresion 1")

def p_expression2(p):
	'''expression : addingOperator term'''
	print ("expresion 2")

def p_expression3(p):
	'''expression : expression addingOperator term'''
	print ("expresion 3")

def p_addingOperator1(p):
	'''addingOperator : PLUS'''
	print ("addingOperator 1")

def p_addingOperator2(p):
	'''addingOperator : MINUS'''
	print ("addingOperator 2")

def p_term1(p):
	'''term : factor'''
	print ("term 1")

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	print ("term 2")

def p_multiplyingOperator1(p):
	'''multiplyingOperator : TIMES'''
	print ("multiplyingOperator 1")

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIVIDE'''
	print ("multiplyingOperator 2")

def p_factor1(p):
	'''factor : ID'''
	print ("factor 1")

def p_factor2(p):
	'''factor : NUM'''
	print ("factor 2")

def p_factor3(p):
	'''factor : LPAREN expression RPAREN'''
	print ("factor 3")

"""
def p_empty(p):
	'''empty :'''
	pass
"""

def p_error(p):
	print ("Error de sintaxis ", p)
#Parte de "main"
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
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print (result)