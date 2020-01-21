package Ush;
import java.util.*;
public class Main {
	final static long mod = 1000000007L;
	static long[] dp = new long [5001];
	public static long go(int num) {		
		if (num == 0) {
			return 1;
		}
		else if (dp[num] >= 0) {
			return dp[num];
		}
		
		dp[num] = 0;
		
		for (int i = 2; i < num+1; i +=2) {
			dp[num] += go(i-2) * go(num- i);
			dp[num] %= mod;
		}
		
		return dp[num];
		
	}
    public static void main(String args[]) {
    	Scanner sc = new Scanner(System.in);
    	Arrays.fill(dp, -1);
    	
    	int testCase = sc.nextInt();
    	
    	while(testCase-- > 0 ) {
    		int len = sc.nextInt();
    		
    		if (len%2 == 0) 
    			System.out.println(go(len));
    		else
    			System.out.println(0);
    	}
    	
    	
    }
}


