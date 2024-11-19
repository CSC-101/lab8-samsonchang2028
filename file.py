
try:
    with open('file_test.txt','r') as file:
        for lines in file:
            if not lines.strip():
                print('Empty Line, error')
                continue
            parts = [part.strip("'") for part in lines.split()]
            print (parts)

            try:
                num1 = float(parts[0])
                print(num1)
                num2 = float(parts[1])
                print(num2)
                line_sum = num1 +num2
                print(line_sum)
            except ValueError:
                print("There are not 2 floats on this line")
                continue

except FileNotFoundError:
    print('File not found!')
    exit()
