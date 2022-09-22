import java.util.Scanner;

public class __1543 {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String document = sc.nextLine();
        String word = sc.nextLine();

        int answer = 0;
        int point = 0;
        while(point != document.length())
        {
            if((point+word.length()-1)<document.length() && document.substring(point, point+word.length()).equals(word))
            {
                answer+=1;
                point = point+word.length();
            }
            else
            {
                point +=1;
            }
        }
        System.out.println(answer);
    }
}
