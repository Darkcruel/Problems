import java.util.Arrays;
import java.util.Scanner;

public class __2012 {
    // https://www.acmicpc.net/problem/2012

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] grade = new int[N];
        long answer = 0;
        for(int i=0;i<N;i++)
        {
            grade[i] = sc.nextInt();
        } // 기대 등수 입력
        Arrays.sort(grade);
        for(int i=0;i<N;i++)
        {
            if(grade[i] >= i+1)
            {
                answer += grade[i]-(i+1);
            }
            else // grade[i] < (i+1)
            {
                answer += (i+1)-grade[i];
            }
        }
        System.out.println(answer);

    }
}
