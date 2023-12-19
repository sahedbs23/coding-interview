package com.moral.sahed.arrays;

import java.util.Arrays;

/**
 * LeetCode Link <a href="https://leetcode.com/problems/sort-an-array/">912. Sort an Array</a>
 */
public class LeetCode912 {
    public static void main(String[] args) {
        int[] arr = new int[]{5,2,3,1};
        int[] arr2 = new int[]{5,1,1,2,0,0};
        System.out.println(Arrays.toString(mergeShort(arr,0,arr.length)));
        System.out.println(Arrays.toString(mergeShort(arr2,0,arr2.length)));
    }
    public static int[] mergeShort(int[] nums, int start, int end){
        if(end-start <= 1){
            return Arrays.copyOfRange(nums, start,end);
        }
        int mid = (start+end) / 2;
        int[] leftSubArr = mergeShort(nums, start, mid);
        int[] rightSubArr = mergeShort(nums, mid, end);
        int totalLength = leftSubArr.length + rightSubArr.length;
        int[] res = new int[totalLength];
        int i=0,j=0, ins=0;
        while(i<leftSubArr.length || j<rightSubArr.length){
            if(i == leftSubArr.length){
                res[ins] = rightSubArr[j];
                j++;
            }else if(j==rightSubArr.length){
                res[ins] = leftSubArr[i];
                i++;
            }else if(leftSubArr[i] <= rightSubArr[j]){
                res[ins] = leftSubArr[i];
                i++;
            }else{
                res[ins] = rightSubArr[j];
                j++;
            }
            ins++;
        }
        return res;
    }
}
