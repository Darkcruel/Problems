import java.util.Scanner;

class __2891
{
    public static void Arrprint(int[] arr)
    {
        for(int i=0;i<arr.length;i++)
        {
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        int num_team = sc.nextInt(); // 전체 팀수
        int num_broken = sc.nextInt(); // 손상된 팀 수
        int num_add = sc.nextInt(); // 추가 카약 있는 팀 수
        
        int[] num_boat = new int[num_team];
        for(int i=0;i<num_team;i++)
        {
            num_boat[i] = 1;
        } // 초기 팀당 보트수는 1로 초기화
        for(int i=0;i<num_broken;i++)
        {
            num_boat[sc.nextInt()-1] -=1;
        } // 배 없어진 팀의 보트개수 -1
        for(int i=0;i<num_add;i++)
        {
            num_boat[sc.nextInt()-1] +=1;
        } // 배 추가로 가지고 온 팀의 보트개수 +1
        
        for(int i=0;i<num_team;i++)
        {
            if(i==0)
            {
                if(num_boat[i]==0 && num_boat[i+1]==2)
                {
                    num_boat[i] = 1;
                    num_boat[i+1] = 1;
                }
            }
            else if(0!=i && i!=num_team-1)
            {
                if(num_boat[i]==0)
                {
                    if(num_boat[i-1]==2)
                    {
                        num_boat[i] = 1;
                        num_boat[i-1] = 1;
                    }
                    else if(num_boat[i-1]==1&&num_boat[i+1]==2)
                    {
                        num_boat[i] = 1;
                        num_boat[i+1] = 1;
                    }
                }
            }
            else
            {
                if(num_boat[i-1]==2)
                {
                    num_boat[i] = 1;
                    num_boat[i-1] = 1;
                }
            }
        }
        Arrprint(num_boat);
        for(int i=0;i<num_team;i++)
        {
            if(num_boat[i]==0)
            {
                answer+=1;
            }
        }
        System.out.println(answer);
    }
}