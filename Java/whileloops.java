
// WHILE LOOPS / DO WHILE

import java.util.Scanner;

public class whileloops {
    public static void main(String[] args) {
        
        // While loop = executes a block of code as lomng as it's condition remains true

        Scanner scanner = new Scanner(System.in);
        String name = "";
    
        while (name.isEmpty()) {
            System.out.println("Enter your name");
            name = scanner.nextLine();

        }

        System.out.println("Hello "+name);

        do {
            System.out.println("Enter your name ");
            name = scanner.nextLine();
        } while (name.isEmpty());


        scanner.close();
        
    }
}
