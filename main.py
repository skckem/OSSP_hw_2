#include <stdio.h>
int main()
{
        char x;
        double y;
        printf("이름을 입력하세요: ");
        scanf("%s", &x);
        printf("학번을 입력하세요: ");
        scanf("%lf", &y);
        printf("<출력>\n");
        printf("이름: %s",x);
        printf("학번: %lf",y);
        return 0;
        }
