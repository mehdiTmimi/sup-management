/* Online C Compiler and Editor */
#include <stdio.h>
// creer une fonction nommee PI qui retourne la valeur du PI = 3.14
float PI(){
    float x;
    x = 3.14;
    return x; // return 3.14
}
float surface(float rayon){
    float surface;
    float x;
    x = PI();
    //surface = rayon * rayon * PI() 
    surface = rayon * rayon * x;
    return surface;
}
int main()
{
printf("la surface d'un certle avec rayon 6 est %f",surface(6));
float nbr = surface(1);
printf("\n%f",nbr);
    float rayon ;
    printf("\ndonnez le rayon");
    scanf("%f",&rayon);
    printf("la surface est %f",surface(rayon));
    return 0;
}
