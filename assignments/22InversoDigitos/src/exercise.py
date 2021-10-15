
def main():
    num = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    l=len(str(num))
    if l<=6:
        if num>0:
            n=int(str(num)[::-1])
            print(n)
        elif num<0:
            numero=num*-1
            n=int(str(numero)[::-1])
            f=n*-1
            print(f)
    else:
        print('Too long')


if __name__=='__main__':
    main()
