# Determinação das Constantes da Fórmula Semi-Empírica de Massa Através de um Algortimo Genético

Este trabalho foi desenvolvido para a disciplina F 887: Física Nuclear ministrada pelo Prof. José Augusto Chinellato no Intituto de Física Gleb Wataghin da Unicamp.

Nosso objetivo é utilizar dados experimentais da energia de ligação de núcleos para encontrar os coeficientes da fórmula semi-empírica de massa através de um algoritmo genético. Os dados utilizados aqui são do banco de dados [Nuclear structure and decay data (NuDat)](https://www.nndc.bnl.gov/nudat3/) oferecido pelo National Nuclear Data Center.

## Intruções e requisitos

Para executar este código mantenha todos os arquivos disponibilizados neste repositório em uma mesma pasta. Acesse esta pasta através do terminal de comando e utilize o comando python (atente-se para utilizar uma versão compatível caso possua mais de uma instalada) para executar o arquivo "main.py", passando como argumento um nome para o arquivo de texto em que os resultados serão salvos. Por exemplo, em um computador com windows 11 e python 3.10.5 o comando fica: 
```bash
python .\main.py --file_name InsiraNomeAqui
```

Este código foi desenvolvido com as seguintes versões do python e seus pacotes:

- python 3.10.5
- pandas 1.4.4
- numpy 1.23.1