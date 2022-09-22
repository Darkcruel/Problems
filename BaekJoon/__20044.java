import java.util.Arrays;
import java.util.Scanner;

public class __20044 {
    // https://www.acmicpc.net/problem/20044
    public static void main(String[] args)
    {
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        n = n*2;
        int[] abilities = new int[n];
        for(int i=0;i<n;i++)
        {
            abilities[i] = sc.nextInt();
        }
        Arrays.sort(abilities);
        for(int i=0;i<n/2;i++)
        {
            if(i==0)
            {
                answer = abilities[i]+abilities[n-1];
            }
            else
            {
                if(abilities[i]+abilities[n-1-i]<answer)
                {
                    answer = abilities[i]+abilities[n-1-i];
                }
            }
        }
        System.out.println(answer);
    }
}
