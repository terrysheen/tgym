print("""
 _____      ____                 
|_   _|    / ___|_   _ _ __ ___  
  | |_____| |  _| | | | '_ ` _ \ 
  | |_____| |_| | |_| | | | | | |
  |_|      \____|\__, |_| |_| |_|
   gym with Terry |___/             \n """)

import time
print (time.strftime("%Y/%m/%d %H:%M"))

r = [0, ]
r_int = [0, ]
tot = [0, ]

while True:
    training = input("\n(t) Training (or continue) \n(s) Save and exit\n \n(x) Exit\n ") 
    if training == str("x"):
        quit()

    if training == str("t"):
        print(r_int[1: ], "Total:", tot)
        while True:
            try:
                val = int(input("Insert row repeats number or (0) to end: \n "))
            except ValueError:
                print("Input numbers only!")
                continue
            else: 
                r.append(int(val))   
                tot[0] += int(r[-1])
                r_int.append(int(r[-1]))
                print(r_int[1: ], "Total:", tot, )
            if val == int("0"):
                del r[-1]
                del r_int[-1]
                break

    if training == str("s"):
        name = input("name your exercise (example: ABS, squats, etc.):\n")
        text = time.strftime("%Y/%m/%d %H:%M") + '  ' + name + '  Total: ' + str(tot) +'  Rows: ' + str(r_int[1:]) + '\n'
        saveFile = open('result.txt' , 'a' )
        saveFile.write (text)
        saveFile.close()
        print(text)
        quit()  

        