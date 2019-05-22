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
dna = open('./files/dna.fasta', 'r')


# def translate_from_dna_to_rna(dna):
    
#     """your code here"""
    
#     return rna


def make_bar_chart(num_of_nucleotides):
    nucleotides = ['A', 'C', 'G', 'T']
    x1 = len(nucleotides) - 0.2
    x2 = len(nucleotides) + 0.2
    y1 = dict.values(num_of_nucleotides[0])
    y2 = dict.values(num_of_nucleotides[1])
    
    fig, ax = plt.subplots()
    ax.bar(x1, y1, width = 0.4)
    ax.bar(x2, y2, width = 0.4)

    ax.set_facecolor('seashell')
    fig.set_figwidth(12)    #  ширина Figure
    fig.set_figheight(6)    #  высота Figure
    fig.set_facecolor('floralwhite')

    plt.show()

def count_nucleotides_for_gene(curr_line, output_file, i):
    nucleotides = ['A', 'C', 'G', 'T']
    
    gene_dict = dict.fromkeys(nucleotides, 0)

    if i > 0:
        ind_name = curr_line.find('\n')
        gene_name = str(curr_line)[:ind_name]
        gene_nucleotides =  str(curr_line)[ind_name:]
        output_file.write(f'{gene_name} \n')
    else:
        gene_nucleotides = curr_line

    for i in nucleotides: 
        gene_dict[i] = gene_nucleotides.count(i)
        output_file.write(f'{i} - {gene_dict[i]} ')
    output_file.write('\n')

    return gene_dict

def count_nucleotides(dna):
    num_of_nucleotides = []
    output_file = open('./files/num_of_nucleotides.txt', 'w')

    gene_name = dna.readline()
    output_file.write(str(gene_name)[1:])
    
    gene_nucleotides = ""
    for i in dna:
        gene_nucleotides += dna.readline()
    splitted_lines = str(gene_nucleotides).split('>')

    for i in range(len(splitted_lines)):
        gene_dict = count_nucleotides_for_gene(splitted_lines[i], output_file, i)
        num_of_nucleotides.append(gene_dict)

    output_file.close()
    return num_of_nucleotides


# def translate_rna_to_protein(rna):
    
#     """your code here"""
    
#     return protein
num_of_nucleotides = count_nucleotides(dna)
print (num_of_nucleotides)
# make_bar_chart(num_of_nucleotides)

dna.close()