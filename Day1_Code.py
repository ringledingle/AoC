with open(r'C:\AOC\Day1_Input.txt', encoding='utf-8') as input_file:
    counter = 0
    input_file.read()
    amount_of_brackets = input_file.tell()
    for loop in range(0,amount_of_brackets + 1):
        input_file.seek(loop)
        reading_symbol = input_file.read(1)
        if (reading_symbol) == "(":
            counter +=1
        elif (reading_symbol) == ")":
            counter -=1
        else:
            break
with open(r'C:\AOC\Day1_Output.log', mode='w', encoding='utf-8') as output_file:
		output_file.write(str(counter))