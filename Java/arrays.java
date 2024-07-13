
// ARRAYS


public class arrays {
    public static void main(String[] args) {
        // Used to store multiple values in a single variable

        String[] cars = {"Camaro","Tesla","Audi","Volvo"};

        cars[3] = "Mustang";

        //System.out.println(cars[3]);
        
        String[] car = new String[3];

        car[0] = "Rolls-Royce";
        car[1] = "Bentley";
        car[2] = "Bugatti";

        for (int i = 0; i < car.length; i++) {
            System.out.println(car[i]);
        }

    }
}
