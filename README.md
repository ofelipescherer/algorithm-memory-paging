<div align=center>
<a href="https://www.python.org">
<img src="https://img.shields.io/badge/python-3.7-informational">
</a>
<a href="https://opensource.org/licenses/MIT">
<img alt="APM" src="https://img.shields.io/apm/l/vim-mode">
</a>
</div>  
    
# Introduction 💡
Memory management in operating systems is one of the big concerns when we're trying to make a system efficient. Paging is a technique that consists of using secondary memory in favor of primary memory.

The name of this technique is justified because the operating system uses the storage of secondary memory in blocks, which are called pages. Each will be mapped with a space in main memory - we call it a frame. That is, each page will be mapped to a frame in memory.

Thus, a main memory will know where that page is in secondary memory, not needing to have all the pages loaded, only need having the mapping.

# About 📘
The project was created to simulate paging in operating systems. This is just for demonstration, it's an easy and visually implementation. If you want to see a real implementation you can take a look at [Simple Snippets](https://www.youtube.com/watch?v=pJ6qrCB8pDw) youtube channel.

Some important things:
- -1 represents a free space in memory;
- RAM, or main memory is limited;
- VRAM, or secondary memory is infinite;
- The number of process, number of pages, and mapping are all random;
- You can test with another values of main memory or the range of these random numbers;

# Objetives 📋

> Demonstrate how a paging works in operating systems

# How Works 👨‍🏫

1. We have two list that represents memories- VRAM and RAM
```python
vram = []
ram = [-1 ] * 10
```
VRAM is infinite, so we don't need to define the start value. But RAM is not, so we defined that RAM has 10 spaces (You can change if you want).

2. We random create some process with a random number of pages with random number of size (You can change if you want).
```python
  number_of_process = randint(1,3)
  for process_id in range(number_of_process):
    process = []
    pages = randint(1,5)
    for page in range(pages):
      size = randint(1,3)
      process.append([process_id , page, size])
      print(f' Process: {process_id}; Page: {page}; Size: {size}')
    vram.append(process)
```

3. We need to create de mapping and add to the RAM.
```python
  for index, value in enumerate(vram):
    mapping = []
    for process in value:
      frame_number = randint(number_of_process+1, len(ram)-1)
      mapping.append([process[1], frame_number])
      print(f'Process {index} page {process[1]} mapped at frame {frame_number}')
    ram[index] = mapping
```

4. And after setting up all these things we can finally simulate the paging
 - First we try to allocate the process into RAM  
```python
in_process = True
  while(in_process):
    for process_index, process in enumerate(vram):
      for page_index, page in enumerate(process):
        if(page[2]!=0):
          mapping = ram[process_index][page_index]
          if(ram[mapping[1]]==-1):
            print(f'Process {page[0]}, page {page[1]}, position {mapping[1]} allocated')
            ram[mapping[1]] = page
            print(f'RAM: {ram}\n')
```
 - Second we need to decrease size of all process that are in RAM
```python
    for i in range(number_of_process, len(ram)):
      if(ram[i]!=-1):
        page = ram[i]
        page[2] = page[2] - 1
        if(page[2]<=0):
          print(f'Removed process {page[0]}, page {page[1]}, position {ram.index(ram[i])} because processing has finished')
          ram[i] = -1
          print(f'RAM: {ram}\n')
```
 - And finally we need to know if still has a process with size greater than 0, if it is, we try do more one loop, if it isn't we can finish the program
```python
    has_process = False
    for i in vram:
      for j in i:
        if(j[2]!=0):
          has_process = True
    
    if(not has_process):
      in_process = False
```

# Run Locally 📂
- You need to install [Python 3](https://www.python.org/downloads) to run the program.

- Do a git clone

      git clone https://github.com/ofelipescherer/algorithm-memory-paging.git

- After you can run `paging.py`

# Reference Material 📚
[Simple Snippets](https://www.youtube.com/watch?v=pJ6qrCB8pDw)

# Legal Informations 👩‍⚖️

- The project is [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
- You can fork and use as you want
- I would appreciate if you put my name and the link to this repository

