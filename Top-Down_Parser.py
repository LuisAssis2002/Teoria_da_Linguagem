def main():
    global s
    global i
    print("Top-Down Parser para sequinte gramática\n")
    print("A1 → aA1A2 | bA2 | aA1BA2 | bBA2 | a\nA2 → aA1 | b | aA1B |bB\nB → aA1A1 | bA1 | aA1BA1 | bBA1 | aA1A1B | bA1B | aA1BA1B | bBA1B\n" )
    print("Entre com uma string: (Atenção - O alfabeto {a,b}) ")
    s = list(input())
    i = 0
    if(A1()):
        if(i==len(s)):
            print("Essa entrada é aceita pela linguagem")
        else:
            print("Essa entrada não é aceita pela linguagem")
        
    else:
        print("Essa entrada não é aceita pela linguagem")

def match(a):
    global s
    global i
    if(i>=len(s)):
        return False
    elif(s[i]==a):
        i+=1
        return True
    else:
        return False

def A1():
    if(match("a")):
        if(A1()):
            if(A2()):
                return True
        elif(B()):
            if(A2()):
                return True
        else:
            return True
    elif(match("b")):
        if(A2()):
            return True
        elif(B()):
            if(A2()):
                return True
    else:
        return False

def A2():
    if(match("a")):
        if(A1()):
            if(B()):
                return True
            else:
                return True
    elif(match("b")):
        if(B()):
            return True
        else:
            return True
    else:
        return False

def B():
    if(match("a")):
        if(A1()):
            if(B()):
                if(A1()):
                    if(B()):
                        return True  
                    else:
                        return True    
            elif(A1()):
                if(B()):
                    return True
                else:
                    return True
    elif(match("b")):
        if(A1()):
            if(B()):
                return True
            else:
                return True
        elif(B()):
            if(A1()):
                if(B()):
                    return True
                else:
                    return True
    else:
        return False
    
main()