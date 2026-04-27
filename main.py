#Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import choice

#cabeçalho de início colorido
print(f"\033[1;31;47m {' BATALHA JO-KEN-PO ':=^60} \033[m")
print(f"\033[37;41m{'SEJA BEM VINDO':^62}\033[m")

#pegando nome do usuario e deixando colorido
nome = input('\033[33mDigite seu nome:\033[m ')
print(f'\033[7;36;47mBoa sorte\033[m \033[31m{nome}\033[m!')
nome_format = f'\033[4;31m{nome}\033[m'

#pegando a jogada do usuário
jogador = input('''Pense na sua jogada e digite:
\033[4;32mPEDRA, PAPEL OU TESOURA.\033[m
Jogue: ''').upper().strip()

#tratamento: se a jogada digitada pelo usuário for incorreta
if jogador not in ['PEDRA', 'PAPEL', 'TESOURA']: #verifica se NÃO tem na lista o valor digitado em jogador.
    print('Jogada Inválida! Tente novamente')
    exit() #para o programa.

#animação colorida jo-ken-po
print(f'\033[31;43mJO \033[m', end='', flush=True) # flush diz: mostra isso agora!
sleep(1)
print(f'\033[37;42mKEN \033[m', end='', flush=True)
sleep(1)
print(f'\033[33;44mPO! \033[m')

#config da escolha do computador + nome do mesmo colorido
computador = ['pedra', 'papel', 'tesoura']
pc = choice(computador).upper()
pc_nome_cor = f'\033[4;31mComputador\033[m'

#hora da batalha
print('-=' * 25)
print(f'{nome_format}: {jogador} vs {pc_nome_cor}: {pc}')
print('-=' * 25)

#variaveis para exibir "venceu" e "perdeu" coloridos.
venceu = '\033[33;41mVENCEU!\033[m'
perdeu = '\033[30;44mPERDEU!\033[m'

#verifica as disputas entre pedra/papel/tesoura
if jogador == 'PEDRA' and pc == 'TESOURA' or jogador == 'TESOURA' and pc == 'PEDRA':
    if jogador == 'PEDRA':
        print(f'\033[33mPedra quebra a tesoura! Você\033[m {venceu}')
    else:
        print(f'\033[34mPedra quebra a tesoura! Você\033[m {perdeu}')
elif jogador == 'PAPEL' and pc == 'PEDRA' or jogador == 'PEDRA' and pc == 'PAPEL':
    if jogador == 'PAPEL':
        print(f'\033[33mPapel enrola a pedra. Você\033[m {venceu}')
    else:
        print(f'\033[34mPapel enrola a pedra. Você\033[m {perdeu}')
elif jogador == 'TESOURA' and pc == 'PAPEL' or jogador == 'PAPEL' and pc == 'TESOURA':
    if jogador == 'TESOURA':
        print(f'\033[33mTesoura corta o papel! Você\033[m {venceu}')
    else:
        print(f'\033[34mTesoura corta o papel! Você\033[m {perdeu}')
else:
    print('\033[31;44mEMPATE!\033[m')

 







