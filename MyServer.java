import java.rmi.*;
import java.rmi.registry.*;
public class MyServer{
public static void main(String args[]){
try{
sum stub=new sumremote();
Naming.rebind("rmi://192.168.56.1/sonoo",stub);
}catch(Exception e){System.out.println(e);}
System.out.println("Establishing connection...");
}
}