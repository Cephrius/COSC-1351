package dataStructures;

import java.util.*;

public class PriortyQueues {
    public static void main(String[] args) {
        // Priority Queue = A FIFO data structure that serves elements
        //                  with the highest priorities first
        //                  before elements with lower priority 
        //                  puts the doubles in ascending order.

        // Collections.reverseOrder() <---- Can reverse the order of the list 


        Queue<String> queue = new PriorityQueue<>(Collections.reverseOrder()); 

        queue.offer("B");
        queue.offer("C");
        queue.offer("F");
        queue.offer("D");
        queue.offer("A");


        while (!queue.isEmpty()) {
            System.out.println(queue.poll());
        
        }
    }
}
