/*
Write a program for implementing Client Server communication model using UDP.
Program which finds entered number is even or odd */

import java.io.*;
import java.net.*;

public class udpServerEO //Server Class
{
    public static void main(String args[])  //Main Function
    {
        try
        {
            DatagramSocket ds = new DatagramSocket(2000); // Creating the endpoint for server
            
            byte b[] = new byte[1024]; // 1 mb of variable storage 

            DatagramPacket dp = new DatagramPacket(b, b.length); //Instantiate DatagramPacket with passing parameters holding the byte array
            
            ds.receive(dp);  //DatagramSocket class invokes a method receive(dp) passing a DatagramPacket in the method

            String str = new String(dp.getData(), 0, dp.getLength()); //Create a string variable pass the parameters of DatagramPacket and describe its length
            
            System.out.println(str);        //Printing the string which has been received from the client (for example 4)
            
            int a = Integer.parseInt(str);   //Now 4 will be stored in variable a

            String s = new String(); // Create a variable s to store the message

            if (a % 2 == 0)   //Mod operation (You check if after division you get the remainder as 0)
                s = "Number is even";
            else
                s = "Number is odd";

            byte b1[] = new byte[1024]; // This time the byte variable is for client message
            
            b1 = s.getBytes();      //Store the message which is in s variable to the byte array

            DatagramPacket dp1 = new DatagramPacket(b1, b1.length, InetAddress.getLocalHost(), 1000);  //Sending and configuring the DatagramPacket for the Socket
            
            ds.send(dp1);  //Using the DatagramSocket send the packet to the client
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    }
}