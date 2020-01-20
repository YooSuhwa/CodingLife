package Ush;
import java.util.Scanner;
public class Main {
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			
			int n = sc.nextInt();			
		
			int[] arr = new int [n];
			for (int i = 0; i < n; i++) {
				arr[i] = sc.nextInt();
			}
			n--;
			
			int limit = 20;
			limit++;

			//i까지의 수를 사용해서 j를 만드는 방법의 수 
			int[][] dp = new int [n][limit];
			
			dp[0][arr[0]] = 1;
			for (int i=1; i<n; i++) {
	            for (int j=0; j< limit; j++) {
	                if (j-arr[i] > -1) {
	                    dp[i][j] += dp[i-1][j-arr[i]];
	                }
	                if (j+arr[i] < limit) {
	                    dp[i][j] += dp[i-1][j+arr[i]];
	                }
	            }
	        }

			System.out.println(dp[n-1][arr[n]]);	
		}
}

