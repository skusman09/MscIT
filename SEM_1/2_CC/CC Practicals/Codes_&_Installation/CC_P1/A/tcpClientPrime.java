import java.net.*;
import java.io.*;

/*Client Program*/

class tcpClientPrime //Class
{
    public static void main(String args[])   //main method
    {
        try
        {
            Socket cs = new Socket("LocalHost", 8001); //Ip address and Port are its parameters  (Parameterized constructor)
            
            BufferedReader infu = new BufferedReader(new InputStreamReader(System.in));     //Characters are accepted as stream in a form of buffer

            System.out.println("Enter a number : ");//To ask enter a number

            int a = Integer.parseInt(infu.readLine());      //Store the entered number by user in an integer variable

            DataOutputStream out = new DataOutputStream(cs.getOutputStream());      //Required to print the information 

            out.writeInt(a);//Display the entered number

            DataInputStream in = new DataInputStream(cs.getInputStream()); 
            
            System.out.println(in.readUTF()); //Get the result from server
            
            cs.close();  //Close your socket connection
        }
        catch(Exception e)
        {
            System.out.println(e.toString());   //Throw the error message
        }
    }
}