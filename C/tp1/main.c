#include <stdio.h>


int nbr1;
int nbr2;
int resultat;


int main(){ 
    printf("bienvenue dans notre premiere application\n");
    printf("veuillez saisir un nombre: ");
    scanf("%d",&nbr1) ;
    printf("merci\n");
    printf("veuillez saisir un autre nombre:");
    scanf("%d",&nbr2);
    printf("merci\n");
    resultat = nbr1 * nbr2;

    printf("%d",resultat);
  return 0;
} 