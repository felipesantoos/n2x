import pandas

spreadsheed = pandas.read_csv("numbers_for_extense.csv")

while True:
    try:
        number = int(input("Digite um número: "))
        if number >= 0 and number <= 1000:
            print(spreadsheed["number"].iloc[number])
        elif number > 1000:
            print("Informe um número inteiro de 0 a 1000!")
        else:
            exit()
    except ValueError:
        print("Informe um número inteiro de 0 a 1000!")
