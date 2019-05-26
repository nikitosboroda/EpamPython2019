""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""


def translate_from_dna_to_rna(dna):
    with open("./out/dna_to_rna.txt", "w") as dna_to_rna:
        for line in dna:
            if '>' in line:
                dna_to_rna.write(line)
            else:
                dna_to_rna.write(line.replace('T', 'U'))
    
    #return rna


def count_nucleotides(dna):
	
	count_nucl = open('./out/count_nucl.txt', 'w')
	num_of_nucleotides = {}
	for line in dna:
		if '>' in line:
			if len(num_of_nucleotides) != 0:
				count_nucl.write(str(num_of_nucleotides)+'\n')
			num_of_nucleotides.clear()
			count_nucl.write(line)
			continue
		for nukleot in line:
			if nukleot == '\n':
				continue
			if nukleot in num_of_nucleotides:
				num_of_nucleotides[nukleot] += 1
			else:
				num_of_nucleotides[nukleot] = 1
				
	if len(num_of_nucleotides) != 0:
				count_nucl.write(str(num_of_nucleotides)+'\n')
	count_nucl.close()
	#return num_of_nucleotides


def translate_rna_to_protein(rna):
    
    """your code here"""
    
    return protein
	
	
# read the file dna.fasta
with open('./files/dna.fasta') as dna:
	count_nucleotides(dna)

with open('./files/dna.fasta') as dna:
	translate_from_dna_to_rna(dna)