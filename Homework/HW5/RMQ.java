import java.lang.Math;
import java.util.Arrays;

//Reference: https://www.topcoder.com/community/competitive-programming/tutorials/...
//...range-minimum-query-and-lowest-common-ancestor/

// the "block/square-root" approach
public class RMQ {
	
	private int[] A; // the integer array being queried
	private int n; // the number of blocks
	private int s; // the number of elements in each block (except for perhaps the last block)
	private int[] M; // M[i] stores the minimum element of block i
	
	public RMQ(int[] intArray) {
		this.A = intArray;
		this.n = (int)Math.ceil(Math.sqrt( (double)A.length ));
		this.s = (int)Math.floor(Math.sqrt( (double)A.length ));
		this.M = new int[n];
		//System.out.println("n: " + n);
		//System.out.println("s: " + s);
		
		int minIndex = 0; // an index in A
		int i = 0; // current block
		while(i < n-1) {
			M[i] = A[minIndex];
			for(int j=1; j<s; j++) {
				if(A[minIndex+j] < M[i]) { M[i] = A[minIndex+j]; }
			}			
			minIndex = minIndex + s;
			i++;
		}
		// handle the last block, which may or may not be of size s
		M[n-1] = A[minIndex++];
		while(minIndex < A.length ) {
			if(A[minIndex] < M[n-1]) { M[n-1] = A[minIndex]; }
			minIndex++;
		}
		if(M.length <= 10) {
			System.out.println("M: " + Arrays.toString(M));
		}
	}
	
	public int rmqa(int i, int j) {
		int minElement = A[i];
		int index = i; // an index in A
		
		// Section 1: the part of the range that occurs to the left of a complete block
		while(index%s != 0){
			if(A[index] < minElement) { minElement = A[index]; }
			index++;			
		}
		
		// Section 2: the part of the range that is covered by complete blocks
		int blockNum = index/s;
		while(index + s < j) {
			if(M[blockNum] < minElement) { minElement = M[blockNum]; }
			index += s;
			blockNum = index/s;
		}
		
		// Section 3: the part of the range that occurs to the right of a complete block
		while(index <= j) {
			if(A[index] < minElement) { minElement = A[index]; }
			index++;
		}
		
		return minElement;
	}
	
}

