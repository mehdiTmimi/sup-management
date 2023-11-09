#include <stdio.h>


int nbr1;
int nbr2;
int resultat;


int main(){ 
    printf("veuillez saisir un nombre: ");
    scanf("%d",&nbr1) ;
    printf("veuillez saisir un autre nombre:");
    scanf("%d",&nbr2);

    resultat = nbr1 * nbr2;

    printf("%d",resultat);
  return 0;
} 