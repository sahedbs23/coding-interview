package com.moral.sahed.background.study;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeShortSolution {
    public static void main(String[] args) {
        List<Integer> unsortedList = Arrays.asList(5,3, 1,2 ,4);
        System.out.println(mergeShort(unsortedList, 0,unsortedList.size()));
    }

    /**
     * divide as much as possible (single element)
     *  if endIndex - startIndex <= 1 return List
     *  divide (startIndex + endIndex) / 2
     *  merge short left part of halves
     *  merge short right part of halves
     *  Conquer part
     *  initialize result lists
     *  initialize two variable with 0 index
     *  loop until left index < left list size && right index < right list size
     *  if left index == left list size
     *      push right[index]
     *      increment right counter
     *  else if right index == right list size
     *      push left[index]
     *      increment left counter
     *  if left[index] <= right[index]
     *      push left[index] to result
     *      increment left counter
     *  else
     *      push right[index] to result
     *      increment right counter
     *
     *
     * @param elements List<Integer>
     * @param startIndex int
     * @param endIndex int
     * @return List<Integer>
     */
    public static List<Integer> mergeShort(List<Integer> elements, int startIndex, int endIndex){
        if (endIndex - startIndex <= 1){
            return elements.subList(startIndex, endIndex);
        }

        int midPinter = (startIndex + endIndex) / 2;
        List<Integer> leftHalf = mergeShort(elements, startIndex, midPinter);
        List<Integer> rightHalf = mergeShort(elements, midPinter, endIndex);
        int leftPointer = 0, rightPointer = 0;
        List<Integer> results = new ArrayList<>();
        while (leftPointer < leftHalf.size() || rightPointer<rightHalf.size()){
            if (leftPointer == leftHalf.size()){
                results.add(rightHalf.get(rightPointer));
                rightPointer++;
            } else if (rightPointer == rightHalf.size()) {
                results.add(leftHalf.get(leftPointer));
                leftPointer++;
            } else if (leftHalf.get(leftPointer) <= rightHalf.get(rightPointer)) {
                results.add(leftHalf.get(leftPointer));
                leftPointer++;
            }else {
                results.add(rightHalf.get(rightPointer));
                rightPointer++;
            }
        }

        return results;
    }
}
