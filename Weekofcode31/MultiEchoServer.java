import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.net.Socket;
import java.net.ServerSocket;

public class Solution implements Runnable {

    private int p;

    public Solution(int p) {
    	this.p = p;
    }

    public void run() {
        ServerSocket server = new ServerSocket(p);
        while (true) {
        	Socket client = server.accept();

        	In in = new In(client);
        	Out out = new Out(client);

        	String s;
        	while((s = in.readLine()) != null) {
        		System.out.println(s);
        	}

        	out.close();
        	in.close();
        	client.close();
        }
    }

    public static void main(String[] args) {
    	for (int p = 4444; p <= 4448; p++) {
    		(new Thread(new Solution(p))).start();
    	}
    }
}