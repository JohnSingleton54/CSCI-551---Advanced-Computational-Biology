# John M. Singleton and Yalan Yin
# CSCI 551 - Advanced Computational Biology
# Mini-Project: "Solving The Correlation Measuring Problem Using A Cardinality Estimation Algorithm"

import mmh3
import math

def main():
	#filename = "AL935263.fna"
	filename = "HPV4.FASTA"
	sequence, seq_name = read_fasta_file(filename)
	#print("\n")
	#print(seq_name)
	#print("\n")
	#print(sequence)

	k = 100
	m = 64
	p = int(math.log(m, 2)) # 2^p = m

	card_est = loglog(sequence, k, m, p)
	print("card_est: ", card_est)

	card = brute_force(sequence, k)
	print("card: ", card)


def loglog(sequence, k, m, p):
	counter = []
	for i in range(m):
		counter.append(0)
	for i in range(len(sequence)-k+1):
		hash_value = mmh3.hash(str(sequence[i:i+k]), signed=False)
		bin_num = str("{:032b}".format(hash_value))
		rev_bin_num = bin_num[::-1]
		j = int(rev_bin_num[:p], 2)
		r = (rev_bin_num[p:]).find('1')
		counter[j] = max(counter[j], r)

	R = (1/m)*sum(counter)
	card_est = 0.39701*m*2**R  # constant on p. 79

	return card_est


def brute_force(sequence, k):
	kmers = {}
	card = 0
	for i in range(len(sequence)-k+1):
		kmer = sequence[i:i+k]
		if kmer not in kmers.keys():
			kmers[kmer] = 1
		else:
			kmers[kmer] = kmers[kmer] + 1
	for key in kmers:
		card += 1
	return card


def read_fasta_file(filename):
	file = open(filename, "r")
	line = file.readline()
	seq_name = line[1:].rstrip()
	line = file.readline()
	i = j = 0
	sequence = ""
	while line:
		sequence = sequence + line.rstrip()
		line = file.readline()
	file.close
	return sequence, seq_name


if __name__ == '__main__':
	main()
	