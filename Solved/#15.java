public class Main {

    public static void main(String[] args) {
        long[][] grid = new long[21][21];

        for(int i = 0 ; i <21; i++){
            grid[0][i] = 1;
            grid[i][0] = 1;
        }

        for (int i = 1; i < 21; i++) {
            for (int j = 1; j < 21; j++) {
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1];
            }
        }

        for (int i = 0; i < 21; i++) {
            for (int j = 0; j < 21; j++) {
                System.out.printf("| %d ", grid[i][j]);
            }
            System.out.println();
        }

        System.out.println(grid[20][20]);
        // answer: 137846528820
    }
}
