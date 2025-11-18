import java.util.Scanner;

public class input2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String name;
        byte age;
        String address;

        System.out.print("Enter your name: ");
        name = sc.nextLine();

        System.out.print("Enter your age: ");
        age = sc.nextByte();

        System.out.println("What is your address: "); 
        address = sc.nextLine(); // Notice the program skips this scan/"input". Check input3.java

        System.out.println("Your name is " + name);
        System.out.println("Your age is " + age);
    }
}