import java.rmi.*;
//Main interface file
public interface sum extends Remote{
public int sum(int x,int y)throws RemoteException;
}