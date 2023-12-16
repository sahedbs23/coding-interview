package com.moral.sahed.background.study;

import java.util.Stack;

public class Recursion {
    public static void main(String[] args) {
        System.out.println(findFactorial(5));
        System.out.println(findFactorial2(5));
        System.out.println(findFactorial2(6));
        System.out.println(findFactorial2(6));
        System.out.println(findFactorial2(7));
    }

    // Solution one using recursion.
    public static int findFactorial(int n){
        // Base case
        if (n <=1){
            return 1;
        }
        // recursive call.
        return n*(findFactorial(n-1));
    }

    // Solution 2 array based.
    public static int findFactorial2(int n){
        Stack<Integer> stack = new Stack<>();

        while (n>0){
            stack.push(n);
            n -= 1;
        }

        int res = 1;
        while (!stack.empty()){
            res *= stack.pop();
        }
        return res;
    }
}
