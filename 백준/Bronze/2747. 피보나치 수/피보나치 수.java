import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        ArrayList<Integer> list = new ArrayList<>();
        list.add(0);
        list.add(1);
        for (int i = 2; i < N+1; i++) {
            list.add(list.get(i-1)+list.get(i-2));
        }

        System.out.println(list.get(N));
    }
}