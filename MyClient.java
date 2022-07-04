import java.rmi.*;
//Client file that requests server
import java.util.Scanner;
public class MyClient{
public static void main(String args[]){
try{
Scanner inp= new Scanner(System.in);
sum stub=(sum)Naming.lookup("rmi://192.168.56.1/sonoo");
System.out.println("Enter the number a: ");
int x = inp.nextInt();
System.out.println("Enter the number b: ");
int y = inp.nextInt();
//System.out.println("Sum (a+b) : ");
int sum1=stub.sum(x,y);
System.out.println(x+y); //Displaying the value
}catch(Exception e){}
}
}