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
			
			int[] dp = new int[k];
			for (int i = 1 ; i < n ; i++) {
				for (int j = k-1; j >0; j--) {
					if (j - w[i] >= 0 ) {
						dp[j] = Math.max(dp[j], dp[j-w[i]]+v[i]);
					}
				}
			}
			System.out.println(dp[k-1]);
	}

}
