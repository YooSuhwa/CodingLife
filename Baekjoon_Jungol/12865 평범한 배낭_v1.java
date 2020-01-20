package Ush;

import java.util.Scanner;
public class Main {
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			int n = sc.nextInt();
			int k = sc.nextInt();
			
			n++;
			k++;
			int[] w = new int[n];
			int[] v = new int[n];

			for (int i = 1 ; i < n; i++) {
				w[i] = sc.nextInt();
				v[i] = sc.nextInt();				
			}
			
			int[][] dp = new int[n][k];
			for (int i = 1 ; i < n ; i++) {
				for (int j = 1; j < k; j++) {
					dp [i][j] = dp[i-1][j];
					if (j - w[i] >= 0 ) {
						dp [i][j] = Math.max(dp[i][j], dp[i-1][j-w[i]]+v[i]);
					}
				}
			}
			System.out.println(dp[n-1][k-1]);
	}

}
