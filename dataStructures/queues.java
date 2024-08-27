package dataStructures;

import java.util.LinkedList;
import java.util.Queue;

public class queues {
    public static void main(String[] args) {
        

        // ******************************************************************************************
        // Queue = FIFO data structure (first in first out) (ex. a line of people)
        //         A collection designed for holding elements prior to processing
        // Linear data structurek
        // 
        //         add = enqueue, offer()
        //         remove = dequeue, poll()

        // ******************************************************************************************

        Queue<String> queue = new LinkedList<String>();

        
        queue.offer("Karen");
        queue.offer("Adam");
        queue.offer("Alexander");
        queue.offer("Matthew");
        
        // System.out.println(queue.peek());
        // queue.poll(); <--- Pulls first from the list
        // queue.element();
        
        // System.out.println(queue.isEmpty()); <---- checks if empty
        // System.out.println(queue.size()); <--- checks the size of the queue
        // System.out.println(queue.contains("Adam")); <----- check if item is in queue
        
        // Where are queues useful?

        // 1. Keyboard buffer (letters should appear on the screen in the order they're pressed)
        // 2. Printer Queue (Print jobs should be completed in order)
        // 3. Used in LinkedLists, PriorityQueues, Breadth-first search
        
        System.out.println(queue);



    }
}
