#PYTHON - SEQUÊNCIA DE NÚMEROS IMPARES COM WHILE

contador = 0 #Utilizado como base para iniciar a contagem.

entrada_usuario = input('Você quer contar até quanto? ')

if entrada_usuario.isdigit(): #Aqui valida se é número ou não.
    entrada_usuario = int(entrada_usuario) #Aqui converte a entrada de string para integer.
    while contador < entrada_usuario: #Aqui inicia o laço
        contador += 3 #ou contador = contador + 1. Essa linha atribui a soma de 1 pra cada registro. Se quiser ir de 2 em 2, alterar aqui.
        if contador % 2 == 0: #Utilizado para excluir os números pares.
            continue #Para pular os números pares dentro do laço.
        if contador == 50:
            break
        print(contador)
else:
    print('Digite um valor válido!') #Excessão utilizada para caso o usuário não digitar números, e digitar letras.
