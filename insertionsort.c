#include <stdio.h>

void display(int array[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d ", array[i]);
    }
}

void insertion_sort(int *array, int size)
{
    int value, i;
    for (i = 0; i < size; i++)
    {
        value = array[i];
        
        while (i > 0 && array[i - 1] > value)
        {
            array[i] = array[i - 1];
            i = i - 1;
        }
        array[i] = value;
    }
}

int main()
{   int n;
    printf("Enter the no of elements:");
    scanf("%d",&n);
    int array[n];
    int size = sizeof(array)/sizeof(int);
    printf("Enter The elements:");
    for(int i=0;i<size;i++)
    {
        scanf("%d",&array[i]);
    }
    insertion_sort(array, size);
    display(array, size);

    return 0;
}
