// Random numbers

import java.util.Random;

public class randomnumbers {
    public static void main(String[] args) {
        
        Random random = new Random();

        //int x = random.nextInt(6)+1;
        double y = random.nextInt();
        boolean z = random.nextBoolean();
        
        System.out.println(z);
    }    
}
