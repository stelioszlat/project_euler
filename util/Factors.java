package util;

import java.util.ArrayList;
import java.util.List;

public class Factors {

    static List<Integer> factors(int number) {
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= number; i++) {
            if (number % i == 0)
                list.add(i);
        }

        return list;
    }
    static int factorial(int number) {
        if (number == 0 || number == 1) {
            return 1;
        }

        return number * factorial(number - 1);
    }
}
