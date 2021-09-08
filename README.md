[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Introduction 💡
O gerenciamento de memória em sistemas operacionais é uma das grandes preocupações quando estamos tentando fazer um sistema eficiente. A paginação é uma técnica que consiste em utilizar a memória secundária em favor da memória primária.

O nome dessa técnica se justifica porque o sistema operacional utiliza o armazenamento da memória secundária em blocos, que são chamados de páginas. Cada uma será mapeada com um espaço na memória principal- damos o nome de frame. Ou seja, cada página será mapeada a um frame na memória. 

Assim, a memória principal saberá onde aquela página está na memória secundaria, não precisando ter todas as páginas carregadas, somente precisará do mapeamento.

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

# Run Locally 📂
- You need to install [Python 3](https://www.python.org/downloads) to run the program.

- Do a git clone

      git clone https://github.com/ofelipescherer/python-memory-paging.git

- After you can run `paging.py`

# Reference Material:
[Simple Snippets](https://www.youtube.com/watch?v=pJ6qrCB8pDw)
























