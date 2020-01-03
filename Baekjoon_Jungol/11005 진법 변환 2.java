/*
	

*/
import java.util.Scanner;
public class Main {

	   public static String convert(int num, int b) {
	 
	        String result = "";
	 
	        while (num > 0) {
	            if (num % b < 10) {
	                result = (num % b) + result;
	                num = num / b;
	            } else {
	                int temp = (num % b) + 55;
	                result = (char)temp + result;
	                num = num / b;
	            }
	        }
	 
	        return result;
	    }
	 
	    public static void main(String[] args) {
	        Scanner sc = new Scanner(System.in);
	 
	        int N = sc.nextInt();
	        int B = sc.nextInt();
	 
	        System.out.println(convert(N, B));
	 
	    }
	}