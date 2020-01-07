# John M. Singleton and Yalan Yin
# CSCI 551 - Advanced Computational Biology
# Mini-Project: ["Solving The Correlation Measuring Problem Using A Cardinality Estimation Algorithm"]
import mmh3
import math
import time
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def main():
	#extract sequences
	filename1 = "HPV4.FASTA"
	sequence1, seq_name1 = read_fasta_file(filename1)

	filename2 = "HPV5.FASTA"
	sequence2, seq_name2 = read_fasta_file(filename2)

	filename3 = "HVV1.FASTA"
	sequence3, seq_name3 = read_fasta_file(filename3)

	#test file for time complexity
	filename4 = "AL935263.FASTA"
	sequence4, seq_name4 = read_fasta_file(filename4)

	#parameters for loglog
	m=64
	p=6
	k=3

	#test for different k in a fixed sequence
	k_arr1=[3,4,5,10,20,50,100,120,200,300,500,1024,2028]
	est_arr=[]
	act_arr=[]
	accuray_arr=[]

	#store the pieces for each sequence
	seq_arr2=[]
	#store the generated number
	temp = []

	for i in range(30):
		#generate the number 1000, 2000, ..., 30,000
		temp.append(1000*(i+1))
		seq_arr2.append(sequence4[:temp[i]])

	#test for time complexity
	#print the size of sequences
	#print(str(len(sequence1)) + " " + str(len(sequence2)) + "    "+ str(len(sequence3)) + "  " + str(len(sequence4)))

	#test for different sequences for multiple k-mers
	seq_arr=[sequence1, sequence2, sequence3]
	k_arr2=[3,4,11]


	#comapring the estimating Cardinality and exact Cardinality using one file and calculate the accuracy
	print('-------------Test for accuracy-----------')
	for i in range (len(k_arr1)):
		log_result = loglog(sequence3,k_arr1[i],m,p)
		est_arr.append(log_result)
		act_result = len(brute_force(sequence3, k_arr1[i]))
		act_arr.append(act_result)
		accuracy = log_result/act_result
		accuray_arr.append(accuracy)
		print("i: " + str(i)+ "  log_result: " + '{:10.4f}'.format(log_result) + "     act_result: " + str(act_result) + "     accuray: " + '{:10.4f}'.format(accuracy))
	print("\n")


	#test for execution time for loglog VS brute_force
	exc_time1 = []
	exc_time2 = []
	print("------------Test For Time Complexity----------")
	for i in range (len(seq_arr2)):
		start_time1 = time.time()
		log_result = loglog(seq_arr2[i],25,m,p)
		exc_time1.append(time.time()-start_time1)
		est_arr.append(log_result)
		start_time2 = time.time()
		act_result = len(brute_force(seq_arr2[i], 25))
		exc_time2.append(time.time()-start_time2)
		#print("sequence size: " + str(len(seq_arr2[i])))

	#plot the execution time for loglog and brute force
	red_patch = mpatches.Patch(color='red', label='LogLog')
	green_patch = mpatches.Patch(color='green', label='brute_force')
	plt.legend(handles=[red_patch, green_patch])
	plt.xlabel('sequence length')
	plt.ylabel('execution time (seconds)')
	plt.plot(temp, exc_time1,marker='o',color='red')
	plt.plot(temp, exc_time2,marker='o',color='green')
	plt.show()
	print("\n")

	#test for time complexity for brute_force
	'''print("-------------Test for brute_force time complexity---------")
	for i in range(len(seq_arr2)):
		print("sequence size: " + str(len(seq_arr2[i])) + "   dictionary size:  " + str(len(brute_force(seq_arr2[i],60))))
	print("\n")'''


#loglog function for estimate Cardinality
def loglog(sequence, k, m, p):
	counter = []
	for i in range(len(sequence)-k+1):
	    counter.append(0)
    #print(counter)
	for i in range(len(sequence)-k+1):
		#get the M= 32 Bit value
		hash_value= mmh3.hash(str(sequence[i:i+k]), signed=False)
		bin_num = str("{:032b}".format(hash_value))
		rev_bin_num = bin_num[::-1]
		j = int(rev_bin_num[:p],2)
		r = rev_bin_num[p:].find('1')#r:rank(number)-find first 1
		counter[j] = max(counter[j],r)

	R = (1/m)*sum(counter)
	card_est = 0.642*m*2**R
	return card_est


#brute force for exact Cardinality
def brute_force(sequence,k):
	kmers = {}
	for i in range(len(sequence)-k+1):
		kmer = sequence[i:i+k]
		if kmer not in kmers.keys():
			kmers[kmer]=1
		else:
			kmers[kmer]=kmers[kmer]+1
	return kmers


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
