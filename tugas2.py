def main():

    for x in range(1,6):
        for y in range(1,6-int(x)):
            print(" ",end="")

        for z in range(1,int(x)+1,1):
            print("*",end="")
        print()

if __name__=="__main__":
    main()
