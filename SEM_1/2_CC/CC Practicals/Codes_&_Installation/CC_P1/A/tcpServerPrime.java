/*Practical 1A: A client server based program using TCP to find if the number entered is prime.*/


/*Server Program*/

import java.net.*;
import java.io.*;

class tcpServerPrime    //Class name should be same as program file name
{
    public static void main(String args[])      //Main Method
    {
        //To detect any operation error or logical erros
        try         
        {

            ServerSocket ss = new ServerSocket(8001);   //Server endpoint

            //Print server is started
            System.out.println("Server Started...............");

            //Accept method
            Socket s = ss.accept();

            //For accepting characters take information
            DataInputStream in = new DataInputStream(s.getInputStream()); 
            
            int x = in.readInt(); //Store the number in x variable
            
            //To print information Characters UTC Encoded
            DataOutputStream otc = new DataOutputStream(s.getOutputStream()); 
            
            int y = x/2;    //store in y variable

            if(x == 1 || x == 2 || x == 3)
            {
                otc.writeUTF(x + "is Prime");       //Directly Print Prime if numbers are 1 2 3
                System.exit(0);
            }
            for(int i = 2; i <= y; i++)
            {
                if(x % i != 0)          //Divide the number and the remainder is your mod (If remainder is no 0 it means it is a prime number)
                {
                    otc.writeUTF(x + " is Prime");
                }
                else
                {
                    otc.writeUTF(x + " is not Prime");
                }
            }
        }
        catch(Exception e)  //Catch your exception
        {
            //Print if any error occurs
            System.out.println(e.toString());
        }
    }
}
