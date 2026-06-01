package util;

import java.util.ArrayList;
import java.util.List;

public class Numbers {

    public static boolean isEven(int number) {
        return number % 2 == 0;
    }

    public static boolean isOdd(int number) {
        return number % 2 == 1;
    }

    public static boolean isTriangular(int number) {
        int sum = 0;
        for (int i = 0; i <= number / 2; i++) {
            sum += i;
        }

        return sum == number;
    }

    public static int triangularTerm(int number) {
        int sum = 0;
        for (int i = 1; i <= number; i++) {
            sum += i;
        }

        return sum;
    }

    public static boolean isPerfect(int number) {
        List<Integer> divs = new ArrayList<>();
        int sum = 0;

        for (int i = 1; i < number; i++) {
            if (number % i == 0) {
                divs.add(i);
            }
        }

        for (int i = 0; i < divs.size(); i++) {
            sum += divs.get(i);
        }

        return sum == number;
    }

    public static boolean isDeficient(int number) {
        boolean s = isPerfect(number);

        return false;
    }

    public static List<Integer> divisorsOf(int number) {
        List<Integer> divisors = new ArrayList<>();

        if (isEven(number)) {
            
        }
        for (int i = 1; i <= (int) Math.floor((double) number / 2); i++) {
            if (number % i == 0) {
                divisors.add(i);
            }
        }

        return divisors;
    }

}
