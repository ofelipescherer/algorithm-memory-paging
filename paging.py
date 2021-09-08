# 1º VRAM is populated with random number of process (3-5)
# 2º Page mapping is generated based on VRAM size

from random import randint, choice

def start_paging(vram, ram):
  number_of_process = randint(1,3)
  for process_id in range(number_of_process): #Populando VRAM
    process = [] #lista do processo atual
    pages = randint(1,5)
    print(f'Processo {process_id} com {pages} páginas adicionado a memória virtual')
    for page in range(pages):
      size = randint(1,3) #tamanho da página (por quantos loops vai ter que rodar, antes de ser concluido)
      process.append([process_id , page, size])
      print(f' Processo: {process_id}; Página: {page}; Tamanho: {size}')
    vram.append(process)
  
  print('\nVirtual RAM ( 1º = id; 2º = nº de página; 3º = tamanho)')
  for i in vram:
    print(i)

  print(f'\nMapeamento das páginas:')
  for index, value in enumerate(vram):
    mapping = []
    for process in value:
      #Essa variavel representa a quantidade de possiveis lugares para alocar paginas, ou seja, os frames
      #Como os primeiros espaços da RAM estão destinados ao mapeamento das paginas, os frames não devem começar no incio da lista
      frame_number = randint(number_of_process+1, len(ram)-1)
      mapping.append([process[1], frame_number]) #Mapeando o page number com o frame number
      print(f'Processo {index} página {process[1]} mapeado em frame {frame_number}')
    ram[index] = mapping

  print('\nMapeamento (1º = nº da página; 2º = nº do frame):')
  for i, v in enumerate(vram):
    print(f'Processo {i}: {ram[i]}')

  print('\nRAM (-1 significa espaço livre):')
  print(f'{ram}\n')
    
  #Processando TUDO
  print('-'*150)
  print('\nPROCESSANDO')
  in_process = True
  while(in_process):
    for process_index, process in enumerate(vram):
      for page_index, page in enumerate(process):
        if(page[2]!=0): #Se entrar significa que precisa ser processado
          mapping = ram[process_index][page_index]
          if(ram[mapping[1]]==-1): #Se entrar significa que o espaço está vago
            print(f'Alocando processo {page[0]}, página {page[1]} em posição {mapping[1]}')
            ram[mapping[1]] = page
            print(f'RAM: {ram}\n')

    print('DIMINUINDO 1 NO TAMANHO\n')
    #Agora subtrairemos 1 da propriedade size, simbolizando que foi processado
    for i in range(number_of_process, len(ram)):
      if(ram[i]!=-1):
        page = ram[i]
        page[2] = page[2] - 1 #Processado na RAM
        if(page[2]<=0): #Acabou o processamento, libere o espaço
          print(f'removeu o processo {page[0]}, página {page[1]} da posição {ram.index(ram[i])} pois terminou seu processamento')
          ram[i] = -1
          print(f'RAM: {ram}\n')
    print(f'RAM depois da diminuição: {ram}\n')

    has_process = False
    for i in vram:
      for j in i:
        if(j[2]!=0): #Se o tamanho de qualquer processo for diferente de 0, significa que ainda há processamento
          has_process = True
    
    if(not has_process):
      in_process = False


vram =[]
ram = [-1] * 10 #RAM tem um espaço finito, neste caso, definimos 10 posições
start_paging(vram, ram)

print('-'*150)
print('Estados finais: ')
print(f'RAM: {ram}')
print(f'VRAM: {vram}')

input("\nAperte enter para finalizar...")