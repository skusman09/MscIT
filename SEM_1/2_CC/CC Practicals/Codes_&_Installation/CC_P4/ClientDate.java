import java.rmi.*;
// import java.io.*;

public class ClientDate
{
    public static void main(String args[]) throws Exception 
    {
        String s1;

        InterDate h1 = (InterDate)Naming.lookup("DS");  //Lookup the registery for the interface and typecast it in h1 variable

        s1 = h1.display();

        System.out.println(s1);
    }

}