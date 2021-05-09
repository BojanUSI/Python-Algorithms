S = [None]*100
# Initial size of stack 100 elements.

TOS = 0
# Top of stack


# Puts element x at the top of the stack
# if space permits.
def push(x):
    global S, TOS
    if TOS < len(S):
        S[TOS] = x
        TOS += 1
    else:
        print('Error: Stack overflow')

def pop():
    global S, TOS
    if TOS > 0:
        TOS -= 1
        return S[TOS]
    else:
        print("Error: Stack underflow")

def is_empty():
    global S, TOS
    return TOS == 0