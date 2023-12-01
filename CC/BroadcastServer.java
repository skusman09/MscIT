import java.net.*;
import java.io.*;
import java.util.*;

public class BroadcastServer
{
    public static final int PORT = 1234;

    public static void main(String args[])throws Exception 
    {
        //Creating a Multicast Socket (one sender multiple receivers)
        MulticastSocket socket;
        DatagramPacket packet;
        InetAddress address;

        // set the multicast address to your local subnet 
        address = InetAddress.getByName("239.1.2.3"); 
        socket = new MulticastSocket();

        // join a Multicast group and send the group messages 
        socket.joinGroup(address);
        byte[] data = null; 
        
        for(;;)
        {
            Thread.sleep(10000); 
            System.out.println("Sending "); 
            String str = ("This is Mehdi Calling...."); 
            data = str.getBytes();
            //Pass the parameters in the constructor of DatagramPacket
            packet = new DatagramPacket(data, str.length(), address, PORT); 
            // Sends the packet 
            socket.send(packet);  //Invoke send() method of MulticastSocket Class
        } 
    } 
} 