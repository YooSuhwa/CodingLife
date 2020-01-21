package Ush;
import java.util.*;
import java.io.*;
public class Main {
	static int[] arr ;
	static int[][] dp;
	public static int go(int s, int e) {
		if (s == e) {
			return 0;
		}
		if (dp[s][e] != -1) {
			return dp[s][e];
		}
		
		int sum = 0;
		int answer =-1;
		
		for (int k = s ; k <=e; k++) {
			sum+= arr[k];
		}
		
		
		for (int k = s; k < e; k++) {
			int temp = go(s,k) + go(k+1,e)+sum;
			
			if(answer == -1 || answer > temp) {
				answer = temp;
			}
		}
		dp[s][e] = answer;
		return answer;
	}
    public static void main(String args[]) throws IOException {
    	BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        
    	int testCase = Integer.valueOf(bf.readLine());
        
        while (testCase-- > 0) {
        	int k = Integer.valueOf(bf.readLine()); //size
        	String[] nums = bf.readLine().split(" ");
        	
        	k++;
        	arr = new int [k];
        	dp = new int [k][k];
        	
        	for (int i = 0; i < k-1; i++) {
        		Arrays.fill(dp[i], -1);
        		arr[i+1] = Integer.valueOf(nums[i]);
        		
        	}
        	
        	System.out.println(go(1,k-1));

        }
    	
    	
    }
}


