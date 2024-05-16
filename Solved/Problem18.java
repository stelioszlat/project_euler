package Solved;

import java.util.*;

public class Problem18 {
    static int[] testTriangle = new int[] {
        3,
        7, 4,
        2, 4, 6,
        8, 5, 9, 3
    };

    static int[] evaluationTriangle = new int[] {
        3,
        10, 7,
        12, 14, 13,
        20, 19, 23, 16
    };
    static int[] testSums = new int[] {
        3,
        0, 0,
        0, 0, 0,
        0, 0, 0, 0
    };
    static int[] triangle = new int[] {
        75,
        95, 64,
        17, 47, 82,
        18, 35, 87, 10,
        20, 4, 82, 47, 65,
        19, 1, 23, 75, 3, 34,
        88, 2, 77, 73, 7, 63, 67,
        99, 65, 4, 28, 6, 16, 70, 92,
        41, 41, 26, 56, 83, 40, 80, 70, 33,
        41, 48, 72, 33, 47, 32, 37, 16, 94, 29,
        53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,
        70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,
        91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,
        63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,
        4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23
    };

    static int[] sums = new int[triangle.length];


    public static void main(String[] args) {
        sums[0] = 75;
        for (int i = 1 ; i < triangle.length; i++) {
            sums[i] = 0;
        }
        int rowElements = 1;
        for (int i = 0, row = 1; i <= triangle.length - 16; i++) {
            int newSum = sums[i] + triangle[i + row];
            if (newSum > sums[i + row]) {
                sums[i + row] = newSum;
            }
            newSum = sums[i] + triangle[i + row + 1];
            sums[i + row + 1] = newSum;

            if (rowElements == row) {
                rowElements = 1;
                row++;
            } else {
                rowElements++;
            }
        }

        for (int i = 0; i < sums.length; i++) {
            System.out.println(sums[i]);
        }

        System.out.println(Arrays.stream(sums).max().orElse(0));
    }
}


// answer: 1074

