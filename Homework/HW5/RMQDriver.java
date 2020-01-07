import java.util.Arrays;
import java.util.Random;

// John M. Singleton
// CSCI 551 HW5 Problem 5

//Reference: https://www.topcoder.com/community/competitive-programming/tutorials/...
//...range-minimum-query-and-lowest-common-ancestor/

public class RMQDriver {
	
	public static void main(String[] args) {
		
		int[] array1 = {1,1,2,3,5,8,13,21,34};
		System.out.println("array1: " + Arrays.toString(array1));
		RMQ rmq1 = new RMQ(array1);
		int minElement = rmq1.rmqa(0, 8);
		System.out.println("The minimum element in the range from 0 to 8 is " + minElement + ".");
		minElement = rmq1.rmqa(2, 7);
		System.out.println("The minimum element in the range from 2 to 7 is " + minElement + ".");
		
		int[] array2 = {2,4,3,1,6,7,8,9,1,7};
		System.out.println("\narray2: " + Arrays.toString(array2));
		RMQ rmq2 = new RMQ(array2);
		minElement = rmq2.rmqa(0, 9);
		System.out.println("The minimum element in the range from 0 to 9 is " + minElement + ".");
		minElement = rmq2.rmqa(4, 8);
		System.out.println("The minimum element in the range from 4 to 8 is " + minElement + ".");
		
		int[] array3 = new int[3000000];
		System.out.println("\narray3 is an array of 3,000,000 random integers with values between 0 and 1,000,000,000");
		Random rd = new Random();
		for( int i = 0; i < array3.length; i++) {
			array3[i] = rd.nextInt(1000000000);
		}
		RMQ rmq3 = new RMQ(array3);
		minElement = rmq3.rmqa(0, array3.length-1);
		System.out.println("The minimum element in the range from 0 to 2,999,999 is " + minElement + ".");
		
	}
	
}

