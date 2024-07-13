package dataStructures;

import java.util.ArrayList;

public class arrayDynamic {
    
    // Dynamic Array

    // Dynamic Array = array that resizes itself as needed while still providing O(1) access
    //  
    // Advantages: 
    // 1. Random access of elements O(1)
    // 2. Good locality of reference and data cache utilization
    // 3. easy to insert/delete at the end

    // Disadvantages:
    // 1. wastes more memory
    // 2. Shifting elements is time consuming 0(n)
    // 3. Expanding/Shrinking the array is time consuming 0(n)
    
    
    public static void main(String[] args)  {
        
        DynamicArray dynamicArray = new DynamicArray(10);

        dynamicArray.add("A");
        dynamicArray.add("B");
        dynamicArray.add("C");
        dynamicArray.add("D");
        dynamicArray.add("E");

        dynamicArray.delete("A");
 
        



        // dynamicArray.insert(0, "X");
        // dynamicArray.delete("A");
        // System.out.println(dynamicArray.search("C"));        

        // dyanamic array info
        System.out.println(dynamicArray);
        System.out.println("size: "+dynamicArray.size);
        System.out.println("capacity: "+dynamicArray.capacity);
        System.out.println("empty: "+ dynamicArray.isEmpty());
    }
}