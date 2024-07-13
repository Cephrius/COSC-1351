package dataStructures;

import java.util.ArrayList;
import java.util.LinkedList;

public class linkedvsArray {
    public static void main(String[] args) {
        LinkedList<Integer> linkedList = new LinkedList<Integer>();
        ArrayList<Integer> arrayList = new ArrayList<Integer>();


        long startTime;
        long endTime;
        long elaspedTime;

        for(int i = 0; i < 1000000; i++){
            linkedList.add(i);
            arrayList.add(i);
        }

        // Linked List 
        startTime = System.nanoTime();

        // linkedList.get(999999);
        //linkedList.get(500000);
        // linkedList.remove(0);
        linkedList.remove(500000);

        endTime = System.nanoTime();

        elaspedTime = endTime - startTime;
        System.out.println("LinkedList: \t" + elaspedTime + " ns");


        // array list
        startTime = System.nanoTime();
        
        // arrayList.get(999999);
        // arrayList.remove(0);
        //arrayList.get(500000);
        arrayList.remove(500000);

        endTime = System.nanoTime();

        elaspedTime = endTime - startTime;
        System.out.println("ArrayList: \t" + elaspedTime + " ns");
    }
}
