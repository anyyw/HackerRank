import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for(int arr_i=0; arr_i < n; arr_i++){
            arr.add(in.nextInt());
        }
        //while(arr.size() != 0) {
        for(int i = 0; i < 20; i++) {
            ArrayList<Integer> newarr = new ArrayList<Integer>();
            System.out.println(arr.size());
            int smallest = arr.get(0);
            for( int num : arr) {
                if(num < smallest) { 
                    smallest = num;
                }
            }
            //System.out.println(smallest);
          
            for( int num : arr ) {
                num -= smallest;
                //System.out.println(num);
                if(num > 0) {newarr.add(num);} 
            }
            arr = newarr;
            
        }
    }
}
