import java.rmi.*;

public interface InterDate extends Remote //Create an Interface and extending the properties of Remote Class (RMI)
{
    public String display() throws Exception;  //Create a method display()
}

