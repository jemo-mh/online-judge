#include<stdio.h>
int main(void)
{

    int fib[42]; //0 1 2  ... ... \0
    fib[0]=1;
    fib[1]=0;
    for(int i=2;i<42;i++)
        {
            fib[i]=fib[i-1]+fib[i-2];
        }
    int t;
    scanf("%d",&t);
    int n;
    for(int i=0;i<t;i++)
    {
        scanf("%d",&n);
        printf("%d %d\n",fib[n], fib[n+1]);
    }
    return 0;
}
