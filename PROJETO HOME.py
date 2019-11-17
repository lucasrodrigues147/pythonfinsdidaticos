from time import sleep
bv = input('''\033[1;30;107m Seja bem vindo, e navegue o quanto quiser através do nosso menu!\nPara navegar você tem opções escolha uma delas e pronto!\033[m''')

valido = 0

while valido != 5:
    print ('''\033[1;30;107m        [1]Menu Principal
        [2]Conversor de Moeda
        [3]Calcular desconto
        [4]Calculadora cientifica
        [5]Calculadora comum\033[m\n''')
    valido = int(input('''\033[1;30;107mQEscolha uma das opções?\033[m\n'''))

    if valido == 1:
        print('''\033[1;30;107m        [1]Menu Principal
                [2]Conversor de Moeda
                [3]Calcular Desconto
                [4]Calculadora cientifica
                [5]Calculadora comum\033[m''')
    elif valido == 2:
        conversor = 0
        while conversor != 2:

            print('''\033[1;30;107m Selecione uma das opções abaixo:
            [1]Real Para Dólar
            {2]Real Para Euro\033[m''')
            conversor = int(input('''\033[1;30;107mDigite o número da opção que você escolheu?\033[m'''))
            if conversor == 1:
                real = float(input('''\033[1;30;107mEntão vamos lá, digite o quanto você quer converter:\033[m'''))
                doleta = (real/3,89)
                print("\033[1;30;107mTudo pronto, você tem em R$ {} e isto resulta em {:.2f} U$. Muito obrigado!\033[m".format(real,doleta))
            elif conversor == 2:
                real = float(input('''\033[1;30;107mEntão vamos lá, digite o quanto você quer converter:\033[m'''))
                euro = (real/4.37)
                print("\033[1;30;107mTudo pronto, você tem em R$ {} e isto resulta em {:.2f} £. Muito obrigado!\033[m".format(real,euro))
                print("\033[1;30;207Está feito, você vai retornar ao menu principal! Abraço.\033[m")
                sleep(2000)

    elif valido == 3:
        print('''\033[1;30;107mJá que quer fazer um calculo de desconto, vamos lá eu te ajudo!\033[m''')
        valor = float(input('\033[1;30;107mDigite o valor que você tem aqui:\033[m'))
        porcento = float(input('\033[1;30;107mDigite o valor do desconto(PorFavor, digite só o número tá ok?! haha)\033[m'))
        desc = valor-(valor/100*porcento)
        print('''\033[1;30;107mOlá, com o desconto de {} você,agora, tem o valor de {}\033[m'''.format(porcento,desc))
        print('''\033[1;30;107mEstá Feito, espero ter ajudado, Abraço!\033[m''')
        sleep(2000)

    elif valido == 4:
            print('''\033[1;30;107m Oi,tá precisando daquela forcinha nos calculos cientificos né? 
            Vem comigo, vou te ajudar \033[m''')
            print('''\033[1;30;107m        [1]Fatorial
            [2]Potenciação
            [3]Logarítmo de base 10
            [4]raiz quadrada
            \033[m''')
            calc = int(input('''\033[1;30;107mEscolha a operação que você deseja fazer!\033[m'''))


    sleep(2000)
