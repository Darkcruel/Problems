import java.util.Arrays;
import java.util.Scanner;

public class __12018 {

    // https://www.acmicpc.net/problem/12018
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 과목수
        int m = sc.nextInt(); // 총 마일리지
        int answer = 0; 
        int total = 0; // 지금까지의 최소 마일리지 총합
        int[] mymile = new int[n]; //각 과목당 최소 마일리지
        for(int i=0;i<n;i++)
        {
            int num_want = sc.nextInt();
            int num_max = sc.nextInt();
            int[] mileage = new int[num_want];
            for(int j=0;j<num_want;j++)
            {
                mileage[j] = sc.nextInt();
            }
            if(num_want < num_max)
            {
                mymile[i] = 1;
            }
            else // if num_want>=num_max
            {
                Arrays.sort(mileage);
                mymile[i] = mileage[num_want-num_max];
            }
        }
        Arrays.sort(mymile); // 정렬
        for(int i=0;i<n;i++)
        {
            total += mymile[i];
            if(total<=m)
            {
                answer+=1;
            }
            else
            {
                break;
            }
        }
        System.out.println(answer);
        
    }
}
