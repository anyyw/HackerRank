import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for(int arr_i=0; arr_i < n; arr_i++){
            arr.add(in.nextInt());
        }

        HashMap<ArrayList<Integer>, Integer> h = new Solution.powerSet(arr);

    }

    public HashMap<ArrayList<Integer>, Integer> powerSet(ArrayList<Integer> oldSet) {
        HashMap<ArrayList<Integer>, Integer> h = new HashMap<ArrayList<Integer>, Integer>;
        if (oldSet.isEmpty()) {
            h.put(new ArrayList<Integer>(), 0)
            return h;
        }
        ArrayList<Integer> list = oldSet;
        int head = list.get(0);
        ArrayList rest = new ArrayList<Integer>(list.subList(1, list.size()));
        for(ArrayList<Integer> set : powerSet(rest).keySet()) {

            int sum = 0;
            for (int a : set) {
                sum += a;
            }
            h.put(set, sum);

            ArrayList newSet = new ArrayList<Integer>();
            sum += head;
            newSet.add(head);
            newSet.addAll(set);
            h.put(newSet, sum);
        }
        return h;
    } 
}