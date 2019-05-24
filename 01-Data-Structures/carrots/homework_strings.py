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
# import matplotlib.pyplot as plt
# read the file dna.fasta
import re 
dna = open('./files/dna.fasta', 'r')
rna = open('./files/translation_from_dna_to_rna.txt', 'r')

def split_file(dna):
    dna = open('./files/dna.fasta', 'r')
    lines = dna.readlines()
    gene_nucleotides = ''
    for i in lines:
        gene_nucleotides += i
    gene_nucleotides = gene_nucleotides.strip('>')
    splitted_lines = str(gene_nucleotides).split('>')
    
    return splitted_lines

def translate_from_dna_to_rna(dna):
    rna = []
    splitted_lines = split_file(dna)
    output_file = open('./files/translation_from_dna_to_rna.txt', 'w')
    
    for i in range(len(splitted_lines)):
        curr_line = splitted_lines[i]
        ind_name = curr_line.find('\n')
        gene_name = str(curr_line)[:ind_name]
        curr_dna =  str(curr_line)[ind_name:]
        curr_rna = curr_dna.replace('T', 'U')
        rna.append(curr_rna)

        output_file.write(f'>{gene_name} \n')
        output_file.write(f'{curr_rna} \n')

    output_file.close()
    
    return rna


# def make_bar_chart(num_of_nucleotides):
#     nucleotides = ['A', 'C', 'G', 'T']
#     x1 = len(nucleotides) - 0.2
#     x2 = len(nucleotides) + 0.2
#     y1 = dict.values(num_of_nucleotides[0])
#     y2 = dict.values(num_of_nucleotides[1])
    
#     fig, ax = plt.subplots()
#     ax.bar(x1, y1, width = 0.4)
#     ax.bar(x2, y2, width = 0.4)

#     ax.set_facecolor('seashell')
#     fig.set_figwidth(12)    #  ширина Figure
#     fig.set_figheight(6)    #  высота Figure
#     fig.set_facecolor('floralwhite')

#     plt.show()

def count_nucleotides_for_gene(curr_line, output_file):
    nucleotides = ['A', 'C', 'G', 'T']
    gene_dict = dict.fromkeys(nucleotides, 0)

    ind_name = curr_line.find('\n')
    gene_name = str(curr_line)[:ind_name]
    gene_nucleotides =  str(curr_line)[ind_name:]
    output_file.write(f'>{gene_name} \n')

    for i in nucleotides: 
        gene_dict[i] = gene_nucleotides.count(i)
        output_file.write(f'{i} - {gene_dict[i]} ')
    output_file.write('\n')

    return gene_dict

def count_nucleotides(dna):
    num_of_nucleotides = []
    output_file = open('./files/num_of_nucleotides.txt', 'w')
    
    splitted_lines = split_file(dna)

    for i in range(len(splitted_lines)):
        gene_dict = count_nucleotides_for_gene(splitted_lines[i], output_file)
        num_of_nucleotides.append(gene_dict)

    output_file.close()
    dna.close()

    return num_of_nucleotides


def translate_rna_to_protein(rna):
    rna_codon_table = open('./files/rna_codon_table.txt', 'r')
    codons = []
    new_values = []
    lines = rna_codon_table.readlines()
    
    for line in lines:
        line = line.replace('\n', '')
        for codon in re.finditer(r'[U,A,C,G]{3}', line):
            codons.append(codon[0])
        for value in re.finditer(r'[^U,^A,^C,^G,^ ]*', line):
            if value[0] != '':
                new_values.append(value[0])
    rules_to_translate = dict(zip(tuple(codons), tuple(new_values)))
    #print(rules_to_translate)

    rna_lines = rna.readlines()
    print(rna_lines)
    # curr_line = splitted_lines[i]
    #     ind_name = curr_line.find('\n')
    #     gene_name = str(curr_line)[:ind_name]
    #     curr_dna =  str(curr_line)[ind_name:]
    #     curr_rna = curr_dna.replace('T', 'U')
    #     rna.append(curr_rna)
    
    
    #return protein
num_of_nucleotides = count_nucleotides(dna)
translate_from_dna_to_rna(dna)
translate_rna_to_protein(rna)
# make_bar_chart(num_of_nucleotides)

dna.close()