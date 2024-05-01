package com.moral.sahed.background.study;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeIntervals {
    public static void main(String[] args) {
        int[][] arr = new int[4][2];
        arr[0] = new int[]{1,3};
        arr[1] = new int[]{2,6};
        arr[2] = new int[]{8,10};
        arr[3] = new int[]{15,18};
        int[][] res = merge(arr);
        for (int[] a: res) {
            System.out.println(Arrays.toString(a));
        }

    }
    public static  int[][] merge(int[][] intervals) {
        int i = 0;
        ArrayList<int[]> list = new ArrayList<>();
        while(i<intervals.length){
            list.add(intervals[i]);
            if(i<intervals.length-1 && intervals[i][1] >= intervals[i+1][0]){
                int[] l = list.get(list.size()-1);
                l[1] = intervals[i+1][1];
                list.set(list.size()-1,l);
                i += 2;
            }else {
                i++;
            }
        }
        return list.toArray(new int[0][]);
    }
}
