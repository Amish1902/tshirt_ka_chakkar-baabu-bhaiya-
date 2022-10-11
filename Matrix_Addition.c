#include <stdio.h>

int main()
{  int r,c,i,j,a[100][100],b[100][100],sum[100][100];
    printf("Enter the no of rows:");
    scanf("%d",&r);
    printf("Enter the no of column:");
    scanf("%d",&c);
    
    printf("Enter the elements of first matrix\n");
    
    for(i=0;i<r;++i)
    for(j=0;j<r;++j)
    {
        printf("Enter the element a%d%d:",i+1,j+1);
        scanf("%d",&a[i][j]);
        
    }
    printf("Enter the elements of second matrix\n");
    
    for(i=0;i<r;++i)
    for(j=0;j<r;++j)
    {
        printf("Enter the element b%d%d:",i+1,j+1);
        scanf("%d",&b[i][j]);
    }
    
    for(i=0;i<r;++i)
    for(j=0;j<r;++j)
    {
        sum[i][j]=a[i][j] + b[i][j];
    }
    
    for(i=0;i<r;++i)
    for(j=0;j<r;++j)
    {
        printf("%d  ",sum[i][j]);
        
        if(j==c-1){
            printf("\n\n");
        }
    }
    
    
    
    


    return 0;
}

