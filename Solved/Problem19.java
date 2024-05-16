package Solved;

import java.time.DayOfWeek;
import java.time.LocalDate;

public class Problem19 {

    public static void main(String[] args) {
        LocalDate startDate = LocalDate.of(1901, 1, 1);
        LocalDate endDate = LocalDate.of(2000, 12, 31);
        LocalDate currentDate = startDate;
        int sundays = 0;
        while (currentDate.isBefore(endDate) || currentDate.isEqual(endDate)) {
            currentDate = currentDate.plusDays(1);

            if (currentDate.getDayOfWeek().equals(DayOfWeek.SUNDAY) && currentDate.getDayOfMonth() == 1) {
                sundays++;
            }
        }

        System.out.println(sundays);
    }
}

// answer 171
