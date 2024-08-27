import java.util.Scanner;

/**
 * nestedloops
 */
public class nestedloops {

    public static void main(String[] args) {
        // loop inside of a loop
        Scanner scanner = new Scanner(System.in);

        int rows;
        int columns;
        String symbol = "";

        System.out.println("Enter amount of rows: ");
        rows = scanner.nextInt();
        System.out.println("Enter amount of columns: ");
        columns = scanner.nextInt();
        System.out.println("Enter symbol to use: ");
        symbol = scanner.next();

        for (int i = 1; i <= rows; i++) {
            System.out.println();
            for (int j = 1; j <= columns; j++) {
                System.out.print(symbol);
            }
        }
    }
}