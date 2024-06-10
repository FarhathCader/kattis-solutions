import java.util.Scanner;
import java.lang.Math;

public class Areal{
   public static void main (String[] args) {
      Scanner scanner = new Scanner(System.in);
      Long area = scanner.nextLong();
      double length = Math.sqrt(area); // Calculate the length of the square
      System.out.println(length * 4); // Calculate the perimeter of the square
   }
}
