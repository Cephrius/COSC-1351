// Array Lists

import java.util.ArrayList;

public class arrayList {
    public static void main(String[] args) {
        // Array List = A resisable array elements can be added and removed after complitation phase able to store reference data types

        ArrayList<String> food = new ArrayList<String>();
        
        food.add("pizza");
        food.add("hamburger");
        food.add("hotdog");

        food.set(0, "sushi");
        food.remove(2);
        food.clear();

        for (int i = 0; i < food.size(); i++) {
            System.out.println(food.get(i));
        }

    }
}
