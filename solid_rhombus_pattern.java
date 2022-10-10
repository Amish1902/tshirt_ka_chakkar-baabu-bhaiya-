import java.util.Scanner;

public class solidRhombus {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		System.out.println("Enter No of Rows");
		int n = s.nextInt();
		for (int i = 1; i <= n; i++) {
			for (int j = i; j <= n - 1; j++) {
				System.out.print(" ");
			}
			for (int k = 1; k <= n; k++) {
				System.out.print("*");
			}
			System.out.println(" ");
		}
	}

}
