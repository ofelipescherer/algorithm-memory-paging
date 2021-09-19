
from random import randint

def createProcess(process_id, options):
  print('\nCriando processos')
  process = [] #lista do processo atual
  pages = randint(options.get("minProcess"),options.get("maxProcess"))
  for page in range(pages):
    quantum = randint(options.get("minPages"),options.get("maxPages")) #quantum da página (por quantos loops vai ter que rodar, antes de ser concluido)
    process.append([process_id , page, quantum])
    print(f' Processo: {process_id}; Página: {page}; Quantum: {quantum} adicionado a VRAM')
  return process

def createMap(process_list, quantity_ram):
  print(f'\nMapeamento das páginas:')
  process_mapping = []

  for value in (process_list):
    #Essa variavel representa a quantidade de possiveis lugares para alocar paginas, ou seja, os frames
    #Como os primeiros espaços da RAM estão destinados ao mapeamento das paginas, os frames não devem começar no incio da lista
    frame_number = randint(0, quantity_ram-1)
    process_mapping.append([value[0], value[1], frame_number]) #Mapeando o page number com o frame number
    print(f' Processo {value[0]} página {value[1]} mapeado em frame {frame_number}')
  return process_mapping


def init(ram, vram, mapping, options):
  quantum_cycle = 0
  while quantum_cycle <= options.get("quantum_cycles"):

    # tentar remover
    #Agora subtrairemos 1 da propriedade quantum, simbolizando que foi processado
    for i in range(len(ram)):
      if(ram[i]!=-1):
        aux_page = ram[i]
        aux_page[2] = aux_page[2] - 1 #Processado na RAM
        print(f'Diminuindo 1 no quantum do processo {aux_page[0]} página {aux_page[1]} faltando mais {aux_page[2]} quantum')
        if(aux_page[2]<=0): #Acabou o processamento, libere o espaço
          print(f'\nremoveu o processo {aux_page[0]}, página {aux_page[1]} da posição {ram.index(ram[i])} pois terminou seu processamento')
          ram[i] = -1
          print(f'RAM: {ram}\n')

    # tentar criar processo
    if(randint(1,5) == 1):
      new_process = createProcess(len(vram), options)
      vram.append(new_process)

      mapping.append(createMap(new_process, len(ram)))
      print('Mapeamento:',mapping)

    # tentar alocar
    for process_index, process in enumerate(vram):
      for page_index, page in enumerate(process):
        if(page[2]!=0): #Precisa tentar alocar
          #Vendo no mapeamento qual é o frame em que deverá ser alocado e se ele está disponível
          mapped_in = mapping[page[0]][page[1]]

          #Verificando se o frame reservado está livre
          if(ram[mapped_in[2]]==-1):
            #Fazendo a alocação
            print(f'\nAlocando processo {page[0]}, página {page[1]} em posição {mapped_in[2]}')
            ram[mapped_in[2]] = page
            print(f'RAM: {ram}\n')
              

    print(f'RAM no fim do ciclo {quantum_cycle}: {ram}\n')        
    print(f'-------------------------------FIM D0 CICLO {quantum_cycle}-------------------------------')
    quantum_cycle += 1 #Termina um clico



ram = [-1] * 10
vram = []
mapping = []
options = {
  "minProcess": 1,
  "maxProcess": 3,
  "minPages": 1,
  "maxPages": 3,
  "quantum_cycles": 50,
}

init(ram, vram, mapping, options)

print('\n-------------------------------ESTADOS FINAIS-------------------------------\n')
print('RAM (-1 significa espaço livre; qualquer outra coisa significa um processo não terminado):')
print(ram)

print('\nVRAM (Legenda: [[[id de processo; id da página; quantum]]])')
print(vram)

print('\nMapeamento (Legenda: [[[id de processo; id da página; nº de frame na memória]]])')
print(mapping)

input("\nAperte enter para finalizar...")