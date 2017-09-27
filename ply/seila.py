import lex
import yacc

reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',

}

tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'IF',
   'THEN',
   'ELSE',
   'WHILE',
   'EQUALS',
   'ID',
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUALS = r'\='
t_WHILE = r'while'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'



def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore  = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


data = '''
if hello = 3 + 4 * 10
  + -20 *2
'''

data2 = '''Tuts
Gangsta '''

data3 = input('''''')


lexer.input(data3)



while True:
    tok = lexer.token()
    if not tok:
        break      
    print(tok)

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_equals(p):
    'expression : expression EQUALS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_if(p):
    'factor : IF'
    p[0] = p[1]

def p_factor_else(p):
    'factor : ELSE'
    p[0] = p[1]

def p_factor_then(p):
    'factor : THEN'
    p[0] = p[1]

def p_factor_while(p):
    'factor : WHILE'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_id(p):
    'factor : ID'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()
