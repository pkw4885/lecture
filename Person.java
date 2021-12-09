package ch08;

public class Person {
    public int height;
    public int weight;
    public String gender; //남성, 여성 이외의 정보가 들어오면, "잘못된 성별을 입력했습니다." 라고 출력하고 싶음 or 선택하게 하고 싶음
    public String name;
    public int age;

    public String info(String gender) {
        return "키가 " + height + "cm 이고, 몸무게가 " + weight + "kg인 " + gender + "이 있습니다. " + "이름은 " + name + "이고, 나이는 " + age + "입니다";
    }

    public Person() {}
    public Person(int height) {
        this.height = height;
    }

    public String showInfo() {

        if (this.gender == "남성") {
            return this.info("남성");
        }
        else if (this.gender == "여성") {
            return this.info("여성");
        }
        else {
            return "잘못된 성별입니다. 남성 or 여성을 입력해주세요";
        }

    }

}
