import os

os.chdir('/home/gary')

os.mkdir('musico')
dire=os.listdir(r"/home/gary")

while True:
    try:

        for a in dire:
            if a.endswith('.mp3'):
                os.rename(f'{a}',f'musico/{a}')
    except:
        print('todos os arquivos mp3 foram salvos')
        break