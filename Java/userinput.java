
// User Input

import java.util.Scanner;

public class userinput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("How old are you: ");
        int age = scanner.nextInt();
        System.out.println("What is your favorite food: ");
        scanner.nextLine();
        String food = scanner.nextLine();

        System.out.println("Hello "+name);
        System.out.println("You are "+age+" years old.");
        System.out.println("You like: "+food);
    }
}
