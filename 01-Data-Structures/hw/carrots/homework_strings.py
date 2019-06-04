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
        rna = []
        stk = ''
        for line in dna:
            if '>' in line:
                rna.append(stk.replace('\n', ''))
                stk = ''
                dna_to_rna.write(line)
            else:
                stk += line.replace('T', 'U')
                dna_to_rna.write(line.replace('T', 'U'))
        rna.append(stk.replace('\n', ''))
    rna.pop(0)
    return rna


def count_nucleotides(dna):
	count_nucl = open('./out/count_nucl1.txt', 'w')
	num_of_nucleotides = {i: 0 for i in 'ACGT'}
	for line in dna:
		if line.startswith('>'):
			if num_of_nucleotides['A'] != 0:
				count_nucl.write(str(num_of_nucleotides)+'\n')
			num_of_nucleotides = {i: 0 for i in 'ACGT'}
			count_nucl.write(line)
			continue
		for sym in 'ACGT':
			num_of_nucleotides[sym] += line.count(sym)
	count_nucl.write(str(num_of_nucleotides)+'\n')
	count_nucl.close()


def translate_rna_to_protein(rna):
	codon = {}
	f = open("./files/rna_codon_table.txt")
	for line in f:
		for i in range(0, len(line.split()), 2):
			codon[line.split()[i]] = line.split()[i + 1]
	#print(codon)
	f.close()
	for cod in codon:
	    if codon[cod] == "Stop"
	        codon[cod] = 'S'
	protein = open('prottttt.txt', 'w')
	for i in range(len(rna)):
	    #print('IIIII',i)
	    for j in range(0, len(rna[i]), 3):
	        #print('JJJJJ',j)
	        if rna[i][j:j+3] not in codon:
	            continue
	        protein.write(codon[rna[i][j:j+3]])
	protein.close()
	

with open('./files/dna.fasta') as dna:
	count_nucleotides(dna)


with open('./files/dna.fasta') as dna:
	rna = translate_from_dna_to_rna(dna)
	#print(rna)
	prot = translate_rna_to_protein(rna)
	#print('PROTEIN', prot)
