package dataStructures;

import java.util.*;

public class LinkedListss {
    public static void main(String[] args) {

        // ************************************************************************************************
        // LinkedList = stores nodes in 2 parts (data + address )
        //              nodes are in non-consecutive memory locations
        //              Elements are linked using pointers

        //                          Singly Linked List
        //            Node                  Node                  Node
        //      [data | address] ->  [data | address]   -->  [data | address]

        //                          Doubly Linked List
        //            Node                                   Node
        //   [address | data | address]     <->     [address | data | address]
        //
        //      advantages?
        //      1. Dynamic data structure ( allocates needed memeory while running)
        //      2. Insertion and deletion of Nodes is easy. O(1)
        //      3. NO/Low memory waste

        //      disadvantages?
        //      1. Greater memory usage (additional pointer)
        //      2. No random access of elements (no index[i])
        //      3. Accessing/searching elements is more time consuming. O(n)


        //      uses?
        //      1. Implements Stacks/Queues
        //      2. GPS navigation
        //      3. music playlist    


        // you can treat a linked list as a stack so functions such as pop() work and can remove elements from your list.
        // offer() adds to the end of a list (tail)
        // push() adds the the front of a list (head)
        
        LinkedList<String> mylist = new LinkedList<String>();

        // mylist.push("A");
        // mylist.push("B");
        // mylist.push("C");
        // mylist.push("D");
        // mylist.push("F");
        // mylist.pop();

        mylist.offer("A");
        mylist.offer("B");
        mylist.offer("C");
        mylist.offer("D");
        mylist.offer("F");

        // mylist.poll();

        mylist.add(4,"E");
        mylist.remove("E");
        // System.out.println(mylist.indexOf("F"));

        System.out.println(mylist.peekFirst());
        System.out.println(mylist.peekLast());

        mylist.addFirst("0");
        mylist.addLast("G");

        String first = mylist.removeFirst();
        String last = mylist.removeLast();

        System.out.println(first);
        System.out.println(last);
        System.out.println(mylist);
    }
};
