class HelloWorld {
    public static void main(String[] args) {
        // declaration d'un objet
        Humain h1;
        // instancier=> reserver de l'espace memoire pour un humain
        h1 = new Humain();
        
        Humain h2 = new Humain();
        
        h1.prenom="mehdi";
        h1.nom="tmimi";
        h1.modifierAge(23);
        int b=h1.lireAge();
        System.out.println(b);
        
        h1.modifierAge(1000);
        b=h1.lireAge();
        System.out.println(b);
        
       /* h2.prenom="hamza";
        h2.nom="berrada";
      //  System.out.println(h1.prenom);
      // System.out.println(h2.prenom);
        h1.salut();
        h2.salut();*/
    }
}
class Humain{
    private String nom;
    public String prenom;
    private int age;
    
    // lire l age
    public int getAge(){
        return age;
    }
    
    // modifier l age
    public void setAge(int a){
        if(a>0 && a<120)
            age=a;
    }
    
    public String getNom(){
        return nom;
    }
    public void setNom(String a)
    {
        nom=a;
    }
     public String getPrenom(){
        return prenom;
    }
    public void setPrenom(String a)
    {
        prenom=a;
    }
    // visibility typeRetour nomFonction(params){
        //contenu
    //}
    public void salut(){
            System.out.println("salut "+nom);
    }
}