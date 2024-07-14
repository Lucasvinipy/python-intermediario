def executar_quiz():
    quiz = [
        { 
            'PERGUNTA': 'QUEM DESCOBRIU O BRASIL?',
            'RESPOSTAS': ['DOM PEDRO', 'PEDRO CABRAL', 'GILBERTO', 'ALFREDO'],
            'CORRETA': 'PEDRO CABRAL'
        },
        { 
            'PERGUNTA': 'QUANTO É 5 + 5?',
            'RESPOSTAS': [10, 20, 5, 7],
            'CORRETA': 10
        },
        { 
            'PERGUNTA': 'QUANTO É 25 * 2?',
            'RESPOSTAS': [50, 100, 75, 25],
            'CORRETA': 50
        },
        {
            'PERGUNTA' : 'QUANTO É 30 / 3?',
            'RESPOSTAS' : [10, 8, 9, 34],
            'CORRETA' : 10
        },
        {
            'PERGUNTA' : 'QUEM É O MAIOR TIME DO BRASIL?',
            'RESPOSTAS' : ['PALMEIRAS', 'SAO PAULO', 'CORINTHIANS', 'UNIAO MOGI'],
            'CORRETA' : 'CORINTHIANS'
        }
    ]

    acertos = 0

    for pergunta in quiz:
        print(pergunta['PERGUNTA'])
        for i, resposta in enumerate(pergunta['RESPOSTAS']):
            print(f"{i + 1}. {resposta}")
        
        while True:
            resposta_usuario = input("Digite o número da resposta correta: ")
            try:
                resposta_usuario = int(resposta_usuario)
                if 1 <= resposta_usuario <= len(pergunta['RESPOSTAS']):
                    break
                else:
                    print("Por favor, digite um número válido.")
            except ValueError:
                print("Por favor, digite um número válido.")

        resposta_correta = pergunta['RESPOSTAS'].index(pergunta['CORRETA']) + 1
        
        if resposta_usuario == resposta_correta:
            print("Correto!\n")
            acertos += 1
        else:
            print(f"Incorreto. A resposta correta é: {pergunta['CORRETA']}\n")

    print(f"Você acertou {acertos} de {len(quiz)} perguntas.")

    if acertos >= 3:
        print("Parabéns! Você foi aprovado.")
    else:
        print("Você não foi aprovado.")
        while True:
            tentar_novamente = input("Deseja tentar novamente? (s/n): ").lower()
            if tentar_novamente == 's':
                executar_quiz()
                break
            elif tentar_novamente == 'n':
                print("Obrigado por participar!")
                break
            else:
                print("Por favor, digite 's' para sim ou 'n' para não.")

executar_quiz()
