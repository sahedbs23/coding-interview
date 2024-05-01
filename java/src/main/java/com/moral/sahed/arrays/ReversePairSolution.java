package com.moral.sahed.arrays;

public class ReversePairSolution {
    public static void main(String[] args) {
        System.out.println(reversePairs(new int[]{1,3,2,3,1})); // 2
        System.out.println(reversePairs(new int[]{2,4,3,5,1})); // 3
        System.out.println(reversePairs(new int[]{1,3,2,3,1,5,7,2})); // 4
    }
    /**
     * Background study
     *  1. BST - Binary Search Tree
     *  2. BIT
     *  3. Merge Short.
     *      1. Recursion
     *          1. Stack
     *      2.Two Pointer
     * @param nums int[]
     * @return int
     */
    public static int reversePairs(int[] nums) {
        int count = 0;
        int i=0,j=nums.length-1;
        while(i<=j){
            if(i<j && nums[i] > 2* nums[j]){
                count++;
            }
            i++;
        }
        return count;
    }
}
