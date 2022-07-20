# Gerador de senhas 

from random import choice

def main():
    quant = int(input('Digite a quantidades de senhas a serem geradas: '))
    tamanho = int(input('Digite o tamanho das senhas: '))
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()_+^~<>/0123456789'
    
    
    with open('Senhas_Geradas.txt', 'a') as arquivo:
        for qtd in range(quant):
            senha = ''
            for cont in range(tamanho):
                senha += choice(char)

            print(f'{qtd+1}° senha: {senha}')

            arquivo.write(f'{qtd+1} senha: {senha}\n')

    print('Suas senhas foram geradas com sucesso!')



if __name__ == '__main__':
    main()