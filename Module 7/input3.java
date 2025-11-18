import java.util.Scanner;

public class input3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String name;
        byte age;
        String address;

        System.out.print("Enter your name: ");
        name = sc.nextLine();

        System.out.print("Enter your age: ");
        age = Byte.parseByte(sc.nextLine());

        System.out.print("What is your address: "); 
        address = sc.nextLine(); 

        System.out.println("Your name is " + name);
        System.out.println("Your age is " + age);
        System.out.println("Your address is " + address);
    }
}