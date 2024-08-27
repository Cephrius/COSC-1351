
// Switches


public class switches {
    public static void main(String[] args) {
        // switches = statement that allows a variable to be test for equalitiy against a list of values

        String day = "Friday";

        switch (day) {
            case "Sunday": System.out.println("It is Sunday");
                break;
            case "Monday": System.out.println("It is Monday");
                break;
            case "Tuesday": System.out.println("It is Tuesday");
                break;
            case "Wednesday": System.out.println("It is Wednesday");
                break;
            case "Thursay": System.out.println("It is Thursday");
                break;
            case "Friday": System.out.println("It is Friday");
                break;
            case "Saturday": System.out.println("It is Saturday");
                break;
            default: System.out.println("That is an invalid day");
                break;
        }
    }
}
