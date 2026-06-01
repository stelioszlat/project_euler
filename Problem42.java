import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Problem42 {
    public static void main(String[] args) {
        Map<Character, Integer> letters = new HashMap<>();
        letters.put('A', 1);
        letters.put('B', 2);
        letters.put('C', 3);
        letters.put('D', 4);
        letters.put('E', 5);
        letters.put('F', 6);
        letters.put('G', 7);
        letters.put('H', 8);
        letters.put('I', 9);
        letters.put('J', 10);
        letters.put('K', 11);
        letters.put('L', 12);
        letters.put('M', 13);
        letters.put('N', 14);
        letters.put('O', 15);
        letters.put('P', 16);
        letters.put('Q', 17);
        letters.put('R', 18);
        letters.put('S', 19);
        letters.put('T', 20);
        letters.put('U', 21);
        letters.put('V', 22);
        letters.put('W', 23);
        letters.put('X', 24);
        letters.put('Y', 25);
        letters.put('Z', 26);

        int letterCount, triangles = 0;
        try {
            String word;
            File file = new File("0042_words.txt");
            Scanner scan = new Scanner(file);

            word = scan.nextLine();
            String[] results = word.split(",");
            for (String result : results) {
                letterCount = 0;
                result = result.replaceAll("\"", "");
                for (int letter = 0; letter < result.length(); letter++) {
                    letterCount += letters.get(result.charAt(letter));
                }

                if (checkIfNumberIsTriangle(letterCount)) triangles++;
            }
        } catch (FileNotFoundException e) {
            System.out.println(e);
        }

        System.out.println(triangles);
    }

    private static boolean checkIfNumberIsTriangle(int number) {
        int n = 1, t;
        while (n < number) {
            t = n * (n + 1) / 2;
            if (t == number) return true;
            n++;
        }
        return false;
    }
}
