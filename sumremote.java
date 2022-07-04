import java.rmi.*;
//remote file for factorial service
import java.rmi.server.*;
public class sumremote extends UnicastRemoteObject implements sum{
sumremote()throws RemoteException{
super();
}
public int sum(int x,int y){
return x+y;
}
}
