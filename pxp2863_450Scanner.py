#Import string
# global variables
charClass=0
lexeme=''
nextChar=''
lexLen=0
token=0
nextToken=0

# function declaration

# Character Classes
LETTER=0
DIGIT=1
UNKNOWN=99
EOF=-1

INT_LIT = 10
IDENT =11
ADD_OP =21
SUB_OP =22
MULT_OP= 23
DIV_OP =24
LEFT_PAREN =25
RIGHT_PAREN =26


f = open("front.in", "r")

def addChar():
    global lexeme
    lexeme+=nextChar
    return
    
    
def getChar():
    global charClass
    global nextChar
    pos=f.tell()
    nextChar=f.read(1)
    pos1=f.tell()
    if(pos==pos1):
        charClass = EOF
    else:
        if(nextChar.isalpha()):
            charClass=LETTER
        elif (nextChar.isdigit()):
            charClass=DIGIT
        else: 
            charClass=UNKNOWN
    return        
            
def getNonBlank():
    global nextChar
    while(nextChar.isspace()):
        getChar()
    return        
    
            
def lookup(char_ch):    
    global nextToken
    if(char_ch=='('):
        addChar()
        nextToken=LEFT_PAREN
    elif     (char_ch==')'):
        addChar()
        nextToken=RIGHT_PAREN
    elif     (char_ch=='+'):
        addChar()
        nextToken=ADD_OP
    elif     (char_ch=='-'):
        addChar()
        nextToken=SUB_OP
    elif     (char_ch=='*'):
        addChar()
        nextToken=MULT_OP
    elif     (char_ch=='/'):
        addChar()
        nextToken=DIV_OP
    else:
        addChar()
        nextToken=EOF
        
    return nextToken
    
    
def lex():
    global lexeme
    global charClass
    global nextToken
    global nextChar
    lexeme=''
    getNonBlank()
    if(charClass==LETTER):
        addChar()
        getChar()
        while(charClass== LETTER or charClass== DIGIT):
            addChar()
            getChar()
        nextToken=IDENT
    elif (charClass==DIGIT):
        addChar()
        getChar()
        while(charClass== DIGIT):
            addChar()
            getChar()
        nextToken=INT_LIT
    elif (charClass==UNKNOWN):
        lookup(nextChar)
        getChar()
    elif (charClass==EOF):
        nextToken= EOF
        lexeme='EOF'
    print("Next token is: ", nextToken ," Next Lexeme is: ",lexeme)
    return
    
        
def main():
        global nextToken
        getChar()
        while(nextToken != EOF):
            lex()
        f.close()   
main()
