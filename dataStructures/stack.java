package dataStructures;

import java.util.Stack;



public class stack {
    public static void main(String[] args) {
        // Stack = LIFO data structure (last in first out)
        //         stores objects into a sort of "vertical tower"
        //         push() to add to the top
        //         pop() to remove from the top

        Stack<String> stack = new Stack<String>();

        
        stack.push("Minecraft");
        stack.push("Fortnite");
        stack.push("Rainbow Six");
        stack.push("Valorant");
        stack.push("CS:GO");
        
        // String myFavGame = stack.pop();

        //stack.pop();

        //System.out.println(stack.empty());
        //System.out.println(stack.peek()); // <----- Looks at the top of the stack without removing it
        //System.out.println(stack.search("CS:GO")); // <----- Finds the number position of item in the stack * the higher the number the lower the item in in the stack
                                                    //         -1 if the function does not find the item
        //System.out.println(stack);

        // System.out.println(myFavGame);

        // for (int i = 0; i < 100000000; i*=2) { <----- RUNNING A OUT OF MEMORY ERROR
        //     stack.push("Fifa Mobile");
        // }

        // uses of a stacks?
        // 1. undo/redo features in text editors
        // 2. moving back/forward throught browser history
        // 3. backtracking algorithms (maze, file directories)
        // 4. calling functions (call stack)




          
    }
}
