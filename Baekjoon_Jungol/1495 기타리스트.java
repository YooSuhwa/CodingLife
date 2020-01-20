import java.util.Scanner;
public class Main {
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			int n = sc.nextInt();
			int start = sc.nextInt();
			int bound = sc.nextInt(); //가능한 볼륨 범위 M
			
			n++;
			bound++;
			
			int[] v = new int [n];
			int [][] dp =  new int [n][bound];
			for (int i = 0; i <n-1; i++) {
				v[i] = sc.nextInt();
			}
			
			dp[0][start] = 1;
			for (int i = 0; i < n-1; i++) {
				for ( int j = 0 ; j < bound ;j++) {
					if (dp[i][j] == 1) {
						if (j - v[i] >=0) {
							dp[i+1][j-v[i]] = 1;
						}
						if (j + v[i]<bound) {
							dp[i+1][j+v[i]] = 1;
						}
					}
					
				}
			}
			
			int flag = -1;
			for (int j = 0; j < bound; j++) {
				if (dp[n-1][j] == 1)
					flag = Math.max(flag, j);
			}	
			
			System.out.println(flag);
	}

}

