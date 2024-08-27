
// For each loop

import java.util.ArrayList;

public class foreachloop {
    public static void main(String[] args) {
        // traversing technique to iterate through the elements in an array/collection, less steps, more readable, less flexible

        //String[] animals = {"cat","dog","rat","eagle"};
        ArrayList<String> animals = new ArrayList<String>();


        for (String i : animals) {
            System.out.println(i);
        }



    }
}
