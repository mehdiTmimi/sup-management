#include <stdio.h>
int main() {
    int nbr;
    printf("donnez un nombre");
    scanf("%d",&nbr);
    if(nbr == 0)
    {
        printf("%d est null",nbr);
    }
    else if(nbr > 0)
    {
        printf("%d est positif",nbr);
    }
    else if(nbr < 0)
    {
        printf("%d est negatif",nbr);
    }
    return 0;
}