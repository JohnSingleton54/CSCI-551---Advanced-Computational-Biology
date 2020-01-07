# John M. Singleton and Yalan Yin
# CSCI 551 - Advanced Computational Biology
# Mini-Project: "Solving The Correlation Measuring Problem Using A Cardinality Estimation Algorithm"

import mmh3
import math

def main():
    #extract sequences
	filename1 = "HPV4.FASTA"
	sequence1, seq_name1 = read_fasta_file(filename1)

	filename2 = "HPV5.FASTA"
	sequence2, seq_name2 = read_fasta_file(filename2)

	filename3 = "HVV1.FASTA"
	sequence3, seq_name3 = read_fasta_file(filename3)

	#extract the first 1000 DNA elements for 3 sequeces
	seq_arr=[sequence1[:1000], sequence2[:1000], sequence3[:1000]]
	k_arr2=[3,4,5,6,7,8,9,10,11,12]

	print("\n----------parameters used-------------------")
	print("m=64")
	print("p=6")
	print("\n-----------tested DNA sequences-------------")
	print("sequence1: " + seq_name1 + "\nsequence2: " + seq_name2 + "\nsequence3: " + seq_name3 +"\n")
	print("\n-------------tested k values----------------")
	print(k_arr2)
	print("\n")

	#parameters for LogLog
	k = 100
	m = 64
	p = int(math.log(m, 2)) # 2^p = m

	card_est = loglog(sequence1, k, m, p)
	#print("card_est: ", card_est)

	card = brute_force(sequence1, k)
	#print("card: ", card)

	#loglog Cardinality tests for 3 sequences with multiple k values
	print ("-------LogLog Cardinality Estimates ---------\n")
	print("k: " + "         3 " + "   4 " + "  5 " + "   6 " + "   7   " + " 8 " + "   9 " + "   10 " + "  11 " + " 12" )
	for i in range(len(seq_arr)):
		temp = "sequence" + str(i+1) + ": "
		for j in range(len(k_arr2)):
			log_result = loglog(seq_arr[i],k_arr2[j],m,p)
			card = 4**(k_arr2[j])
			temp = temp + str(int(log_result)) + "  "
		print(temp)
	print("\n")

	#proporties tests for 3 sequences with multiple k values
	print("-------------Cardinality/4^k----------------\n")
	print("k: " + "            3 " + "           4 " + "          5 " + "          6 " + "         7   " + "         8 " + "          9 " + "         10 " + "         11 " + "         12" )

	for i in range(len(seq_arr)):
		temp = "sequence" + str(i+1) + ": "
		for j in range(len(k_arr2)):
			log_result = loglog(seq_arr[i],k_arr2[j],m,p)
			card = 4**(k_arr2[j])
			temp = temp + str("{:01.8f}".format(log_result/card)) + "  "
		print(temp)

#loglog function for estimate Cardinality
def loglog(sequence, k, m, p):
	counter = []
	for i in range(m):
		counter.append(0)
	for i in range(len(sequence)-k+1):
		hash_value = mmh3.hash(str(sequence[i:i+k]), signed=False)
		bin_num = str("{:032b}".format(hash_value))
		rev_bin_num = bin_num[::-1]
		j = int(rev_bin_num[:p], 2)
		r = (rev_bin_num[p:]).find('1')		#print(key)

		counter[j] = max(counter[j], r)

	R = (1/m)*sum(counter)
	card_est = 0.39701*m*2**R  # constant on p. 79
	return card_est

#brute force function for exact Cardinality
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
