
// 2d Array List
import java.util.*;

import javax.swing.JList.DropLocation;

public class twodarraylist {
    public static void main(String[] args) {
        // a dynamic list of list
        // change the size during runtime
        ArrayList<ArrayList<String>> shoppingList = new ArrayList();

        ArrayList<String> bakeryList = new ArrayList<String>();
        bakeryList.add("pasta");
        bakeryList.add("garlic bread");
        bakeryList.add("dounts");
        

        ArrayList<String> produceList = new ArrayList<String>();
        produceList.add("tomato");
        produceList.add("zucchini");
        produceList.add("peppers");


        ArrayList<String> drinksList = new ArrayList<String>();
        drinksList.add("Coke");
        drinksList.add("Dr.Pepper");
        drinksList.add("Fanta");

        shoppingList.add(bakeryList);
        shoppingList.add(produceList);
        shoppingList.add(drinksList);

        System.out.println(shoppingList.get(0).get(2));
    }
}
