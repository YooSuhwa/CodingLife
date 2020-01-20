import java.util.*;
public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        
        int limit = 20;
        limit++;
        n --;
        
        long[][] d = new long [n][limit];
        d[0][arr[0]] = 1;
        
        for (int i=1; i<n; i++) {
            for (int j=0; j<=20; j++) {
                if (j-arr[i] >= 0) {
                    d[i][j] += d[i-1][j-arr[i]];
                }
                if (j+arr[i] <= 20) {
                    d[i][j] += d[i-1][j+arr[i]];
                }
            }
        }
        System.out.println(d[n-1][arr[n]]);
    }
}