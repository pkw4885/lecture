package ch08;

public class PersonTest {
    public static void main(String[] args) {
        Person james = new Person();

        james.height = 180;
        james.gender = "남";
        james.age = 23;
        james.name = "james";
        System.out.println(james.showInfo());

    }
}
