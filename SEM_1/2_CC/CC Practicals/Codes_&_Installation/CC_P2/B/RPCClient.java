/*
Write a program for implementing Client Server communication model using UDP.
A program to implement simple calculator operations like addition, subtraction, multiplication and division.*/  

import java.io.*;
import java.net.*;
class RPCClient
{
    RPCClient()
    {
        try
        {
            InetAddress ia = InetAddress.getLocalHost();

            DatagramSocket ds = new DatagramSocket();

            DatagramSocket ds1 = new DatagramSocket(1300);

            System.out.println("\nRPC Client\n");

            System.out.println("Enter method name and parameter like add 3 4\n");

            while (true)
            {
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

                String str = br.readLine();

                byte b[] = str.getBytes();

                DatagramPacket dp = new DatagramPacket(b,b.length,ia,1200);

                ds.send(dp);

                dp = new DatagramPacket(b,b.length);

                ds1.receive(dp);

                String s = new String(dp.getData(),0,dp.getLength()); 

                System.out.println("\nResult = " + s + "\n");
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }

    public static void main(String[] args)
    {
        new RPCClient();
    }
}