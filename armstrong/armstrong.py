def main(): 
    fout = open("armstrong.txt", "w")
    try:
        with open("numbers.txt", "r") as fin:
            for line in fin:
                # print(int(line.strip()))
                numString=line.strip()
                x = int(numString)
                l = len(numString)
                if (l==1):
                    fout.write(str(x))
                    fout.write('\n')
                else:
                    y=0
                    for i in numString:
                        y=y+(int(i)**l)
                    if x==y:
                        fout.write(str(x))
                        fout.write('\n')

    except FileNotFoundError:
        print("file not found")
    except:
        print("error opening the input file")
    
    fout.close()


if __name__ == "__main__":
    main()
