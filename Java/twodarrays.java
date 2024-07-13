
// 2D Arrays


public class twodarrays {
    
    public static void main(String[] args) {
        // array of arrays rows and columns

        String[][] cars = new String [3][3];

        cars[0][0] = "Camaro";
        cars[0][1] = "Mustang";
        cars[0][2] = "Model S";
        
        cars[1][0] = "Veyron";
        cars[1][1] = "GT3RS";
        cars[1][2] = "Huracan";

        cars[2][0] = "Aventador";
        cars[2][1] = "Model 3";
        cars[2][2] = "Model Y";


        for (int i = 0; i < cars.length; i++) {
            System.out.println();
            for (int j = 0; j < cars[i].length; j++) {
                System.out.println(cars[i][j] + " ");
            }
        }


        String[][] newCars = {  {"Camaro","Mustang","Model S"},
                                {"Veyron","GT3RS","Huracan"},
                                {"Aventador","Model 3", "Model Y"}
                        };
        for (int i = 0; i < newCars.length; i++) {
            System.out.println();
            for (int j = 0; j < newCars[i].length; j++) {
                System.out.println(newCars[i][j]);
            }
        }
    }
}
