
from random import randint

def createProcess(process_id, options):
  print('\nCreating Process')
  process = [] #Process List
  pages = randint(options.get("minProcess"),options.get("maxProcess"))
  for page in range(pages):
    quantum = randint(options.get("minPages"),options.get("maxPages")) #Page quantum (How many cycles will do)
    process.append([process_id , page, quantum])
    print(f' Process: {process_id}; Page: {page}; Quantum: {quantum} add into VRAM')
  return process

def createMap(process_list, quantity_ram):
  print(f"\Maping's pages:")
  process_mapping = []

  for value in (process_list):
    #Memory frames
    frame_number = randint(0, quantity_ram-1)
    process_mapping.append([value[0], value[1], frame_number]) #Maping frame number with page number
    print(f' Process {value[0]} page {value[1]} mapped in frame {frame_number}')
  return process_mapping


def init(ram, vram, mapping, options):
  quantum_cycle = 0
  while quantum_cycle <= options.get("quantum_cycles"):

    #try removing process
    #Now we are going to try to decrease one of page quantum in memory
    for i in range(len(ram)):
      if(ram[i]!=-1):
        aux_page = ram[i]
        aux_page[2] = aux_page[2] - 1 #Processed in RAM
        print(f"Decreasing 1 in quantum's page {aux_page[0]} page {aux_page[1]} missing {aux_page[2]} quantum")
        if(aux_page[2]<=0): #Processing is finished, free this space
          print(f'\nProcess {aux_page[0]}, page {aux_page[1]} position {ram.index(ram[i])} removed because processing is over')
          ram[i] = -1
          print(f'RAM: {ram}\n')

    #try create process
    if(randint(1,5) == 1):
      new_process = createProcess(len(vram), options)
      vram.append(new_process)

      mapping.append(createMap(new_process, len(ram)))
      print('Mapping:',mapping)

    #try allocate process
    for process_index, process in enumerate(vram):
      for page_index, page in enumerate(process):
        if(page[2]!=0): #If quantum is not 0, try to allocate
          #Now we search for the frame number in maping list
          mapped_in = mapping[page[0]][page[1]]

          #Verifing if this frame is free
          if(ram[mapped_in[2]]==-1):
            #Doing the allocation
            print(f'\nAllocation process {page[0]}, page {page[1]} in position {mapped_in[2]}')
            ram[mapped_in[2]] = page
            print(f'RAM: {ram}\n')
              

    print(f'RAM at end of cycle {quantum_cycle}: {ram}\n')        
    print(f'-------------------------------End Cycle {quantum_cycle}-------------------------------\n')
    quantum_cycle += 1 #finish one cycle



ram = [-1] * 10
vram = []
mapping = []
options = {
  "minProcess": 1,
  "maxProcess": 5,
  "minPages": 1,
  "maxPages": 5,
  "quantum_cycles": 50,
}

init(ram, vram, mapping, options)

print('\n-------------------------------Final States-------------------------------\n')
print('RAM (-1 means a free space; anything else is a process):')
print(ram)

print("\nVRAM (Subtitle: [[[process's id; page's id; quantum]]])")
print(vram)

print("\Mapping (Subtitle: [[[process's id; page's id; frame's number]]])")
print(mapping)

input("\nPress enter to finish...")