import java.rmi.*;
import java.rmi.server.*;
import java.util.*;

public class ServerDate extends UnicastRemoteObject implements InterDate   //Implementing the Remote Interface 
{

    public ServerDate() throws Exception
    {
    }

    public String display() throws Exception
    {
        String str = "";
        Date d = new Date();
        str = d.toString();   //Save Today's Date in str variable
        return str;
    }

    public static void main(String args[]) throws Exception 
    {
        ServerDate s1 = new ServerDate();

        Naming.bind("DS", s1);  //Bind the server to the RMI Registry

        System.out.println("Object registered.....");
    }
}