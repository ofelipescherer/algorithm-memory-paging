# 1º VRAM is populated with random number of process (3-5)
# 2º Page mapping is generated based on VRAM size

from random import randint

def start_paging(vram, ram):
  number_of_process = randint(1,3)
  for process_id in range(number_of_process): #VRAM is populated
    process = [] #List of curently processes
    pages = randint(1,5)
    print(f'Process {process_id} with {pages} pages added to virtual RAM')
    for page in range(pages):
      size = randint(1,3) #Page's quantum (How many cycles to end process)
      process.append([process_id , page, size])
      print(f' Process: {process_id}; Page: {page}; Quantum: {size}')
    vram.append(process)
  
  print('\nVirtual RAM ( 1º = id; 2º = page number; 3º = quantum)')
  for i in vram:
    print(i)

  print(f'\nPage Maping')
  for index, value in enumerate(vram):
    mapping = []
    for process in value:
      #This variable represents where the page needs to go in RAM frame
      #As the first spaces in RAM are intended for page mapping, frames should not start at the top of the list.
      frame_number = randint(number_of_process+1, len(ram)-1)
      mapping.append([process[1], frame_number]) #Maping page number with frame number
      print(f'Process {index} page {process[1]} maped in {frame_number} frame')
    ram[index] = mapping

  print('\nMaping( 1º page number; 2º frame number):')
  for i, v in enumerate(vram):
    print(f'Process {i}: {ram[i]}')

  print('\nRAM (-1 means a free space):')
  print(f'{ram}\n')
    
  #Processing
  print('-'*150)
  print('\nProcessing')
  in_process = True
  while(in_process):
    for process_index, process in enumerate(vram):
      for page_index, page in enumerate(process):
        if(page[2]!=0): #If enters means it needs to be processed.
          mapping = ram[process_index][page_index]
          if(ram[mapping[1]]==-1): #If enters means the space is free
            print(f'Allocating Process {page[0]}, page {page[1]} quantum: {mapping[1]}')
            ram[mapping[1]] = page
            print(f'RAM: {ram}\n')

    print('DECREASE 1 IN QUANTUM\n')
    #Now we will subtract 1 from the size property, symbolizing that it has been processed.
    for i in range(number_of_process, len(ram)):
      if(ram[i]!=-1):
        page = ram[i]
        page[2] = page[2] - 1 #Processed in RAM
        if(page[2]<=0): #Finished processing, free up space
          print(f'Process {page[0]}, page {page[1]} quantum {ram.index(ram[i])} was removed because it finished')
          ram[i] = -1
          print(f'RAM: {ram}\n')
    print(f'RAM after decrease: {ram}\n')

    has_process = False
    for i in vram:
      for j in i:
        if(j[2]!=0): #If the quantum of any Process is different from 0, it means that there is still processing
          has_process = True
    
    if(not has_process):
      in_process = False


vram =[]
ram = [-1] * 10 #RAM has a finite space, in this case we define 10 positions
start_paging(vram, ram)

print('-'*150)
print('End states: ')
print(f'RAM: {ram}')
print(f'VRAM: {vram}')

input("\nPress enter to finish...")