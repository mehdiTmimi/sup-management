class HelloWorld {
    public static void main(String[] args) {
        Human h1 = new Human("tmimi",22);
        System.out.print(h1.nom+ " " + h1.age);
    }
}
class Human{
    public String nom;
    public int age;
    public Human(){
        System.out.println("appel constructeur sans params");
        nom="";
        age=18;
    }
    public Human(String nomV){
        System.out.println("appel constructeur avec 1 param");
        nom = nomV;
        age = 18;
    }
    public Human(String nomV, int ageV){
        System.out.println("appel constructeur avec 2 params");
        nom = nomV;
        age = ageV;
    }
}