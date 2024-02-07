// Swift 클래스 복습

// 클래스를 하나 만든다면 클래스에서 생성된 객체인 인스턴스를 만들어 실제 작업에 쓰일 수 있게 한다.

class Name {
    // 여기서 클래스 안의 변수는 속성(Property)라고 한다.
    var name = "Shin"
    
    // 여기서 클래스 안의 함수는 메소드(Method)라고 한다.
    func my_name() {
        print("my name is \(name)")
    }
}

// let shin : Name = Name()

// print(shin.name)
// shin.my_name()

// shin.name = "Park"
// shin.my_name()


// MARK: 클래스의 상속
// 클래스의 이점은 바로 상속을 이용한 프로그램의 재사용이다.
// 위의 Name이라는 클래스를 슈퍼클래스로 두고 아래 새 클래스에 상속을 걸어보자.

class YourName : Name {  //클래스 상속!!
    var yourName = "Park"
    
    func ourName() {
        print("my name is \(name) and your name is \(yourName)")
    }
}
let shin : YourName = YourName()

print(shin.name)     //"Shin" 출력
print(shin.yourName) //"Park" 출력

shin.my_name() //클래스 상속으로 my_name()메소드 사용 가능
shin.ourName()

// YourName 클래스에는 name, my_name이 없지만 사용이 가능하다!!

// MARK: 클래스의 초기화
// 원하는 인수를 미리 만들어 놓기!!

class Name {
    var name : String
    var age : Int
    
    init(name:String, age:Int) { //초기화!
        self.name = name
        self.age = age
    }
    
    func my_name() {
        print("my name is \(name) and \(age) year's old")
    }
}

let name1 : Name = Name(name: "song", age: 24)
let name2 : Name = Name(name: "kim", age: 25)

name1.my_name()
name2.my_name()

// init(name: , age: ) 메소드를 통해서 인스턴스를 바로 생성해준다!
// 잘 사용해보자!