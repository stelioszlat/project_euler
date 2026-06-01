public class Problem14 {

    public static void main(String[] args) {

        final int MAX = 1000000;

        int n = 13;
        int maxListNumber = 0;

        for (int i = n; i <= MAX; i++) {
            System.out.println(i);
            int t = i;
            int listCount = 0;
            while (t != 1) {
                if (t % 2 == 0) t = t / 2;
                else t = t * 3 + 1;
                listCount++;
            }

            if (listCount > maxListNumber) maxListNumber = i;
        }

        System.out.println(maxListNumber);
    }
}
