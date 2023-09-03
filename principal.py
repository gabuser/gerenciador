import os

print('---->bem vindo ao gerenciador de arquivos.mp3 simples<----')

caminho=input('insira o caminho ex(/home/luffy):')
os.chdir(caminho)
print(f'seu path atual: {os.getcwd()}')

pasta=input('escolha o nome da pasta que deseja armazenar os arquivos:')
os.mkdir(pasta)

def musica(arquivo,dire):
    dire=os.listdir()

    try:
        while True:
            for arquivo in dire:
                if arquivo.endswith('.mp3'):
                    os.rename(f'{arquivo}', f'{pasta}/{arquivo}')
    except:
        print('itens salvos')
musica(0,0)