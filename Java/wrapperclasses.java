
// Wrapper Classes


public class wrapperclasses {
    public static void main(String[] args) {
        // wrapper classes = provides a way to use primitive data types as reference data types
        //                   reference data types contain useful methods
        //                   can be used with collections (ex. ArrayList)


        // Primitive        // wrapper 
        //----------        ----------
        // Boolean          Boolean
        // char             Character
        // int              Integer
        // double           double


        // autoboxing = the automatic conversion that the java compiler make between the primitive type and their corresponding object wrapper class
        // Unboxing = the reverse of autoboxing. Automatic conversion of wrapper class to primitive

        Boolean a = true;
        Character b = '@';
        Integer c = 123;
        Double d = 3.14;
        String e = "Chiedozie";

        // Unboxing Feature
        if (a==true) {
           System.out.println("This is true"); 
        }

    }    
}
