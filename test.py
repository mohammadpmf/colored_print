GRAY        = GR = "\033[90m"
RED         = R  = "\033[91m"
GREEN       = G  = "\033[92m"
YELLOW      = Y  = "\033[93m"
BLUE        = B  = "\033[94m"
PURPLE      = P  = "\033[95m"
LIGHTBLUE   = LB = "\033[96m"
WHITE       = W  = "\033[97m"

ORDINARY    = O  = "\033[0m"
BOLD        = BO = "\033[1m"
ITALIC      = I  = "\033[3m"
UNDERLINE   = U  = "\033[4m"

def colored_print(text, n=1, *args):
    length = len(args)
    i = 0
    i2= 0
    while i<len(text):
        print(args[i2%length],end='')
        print(text[i:i+n], end='')
        i2+=1
        i+=n
    print()

colored_print('Welcome to colored_print function!!!!!!!!', 2,R,G,U,O,B)

