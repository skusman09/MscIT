/*
Write a program for implementing Client Server communication model using UDP.
Program which finds entered number is even or odd */

import java.io.*;
import java.net.*;
public class udpClientEO    //Client Class
{
    public static void main(String args[])
    {
        try
        {
            DatagramSocket ds = new DatagramSocket(1000); //Create a DS for Client
            
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));   //Capture the user's input  

            System.out.println("Enter a number : ");        //Message asking user for entering the number

            String num = br.readLine();     //Reads the entered number on the command prompt then storing it in the num variable

            byte b[] = new byte[1024];  //Create a byte memory to send the message to the server

            b = num.getBytes();  //Get the string characters from the num variable and store it in the b variable

            DatagramPacket dp = new DatagramPacket(b, b.length,InetAddress.getLocalHost(), 2000);  //Datagram Packet configuring the byte, the IP address and port

            ds.send(dp);     //Send the number to the server using DataSocket and pass the Datagram Packet

            byte b1[] = new byte[1024];  //Create a byte variable 

            DatagramPacket dp1 = new DatagramPacket(b1, b1.length); 
            
            ds.receive(dp1);  //The result coming from the server will be received by the client

            String str = new String(dp1.getData(), 0, dp1.getLength());     //Converting the byte information to string 
            
            System.out.println(str);            //Print the result
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    }
}