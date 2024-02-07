// Swift 클로저 복습

// 함수에는 이름이 있는 함수와 없는 함수가 있다!
// 클로저에는 이름이 있는 클로저가 있고 없는 클로저가 있다.
func doSomething() {
    print("Ted")
}
// 이건 named Closure이고 이걸 우리는 함수라고 부른다!!

// 바로 이렇게
// let closure= { print("Ted") }
// 이름을 붙이지 않고 사용하는 함수를 우리는 클로저라고 한다.
// 이것도 마찬가지로 함수의 특성을 갖기에 1급 객체 함수의 특성을 고대로 갖고있다.

// 따라서 클로저도 자료형이 있다는 점!

// { (Parameters) -> Return Type in  실행구문} 이런 식으로 이루어진다.


// (Parameters) -> Return Type 가 Closure Head에 해당하고 
// 실행구문이 Closure 바디에 해당한다.

// 파라미터와 Return Type이 없다면 다음과 같이 사용한다.
// let closure = { () -> () in
//     print("Closure")
// }

// 만약에 둘 다 있다면?
let closure = { (name: String) -> String in
    return "Hello, \(name)"
}
// 다음과 같이 쓴다는 것이다!!
// 하지만 여기서 name은 단순히 Parameter일 뿐 Argument Label은 아니다!

// 1. Closure는 변수나 상수에 대입이 가능하고 대입과 동시에 작성도 된다.
// 2. 함수의 파라미터 타입으로 클로저를 전달할 수 있다. 즉 함수호출 생략이 된다.
// 3. 함수의 반환 타입으로 클로저를 사용할 수 있다!

// 그러나 실제 값을 return할 때의 함수가아닌 
func doSomething() -> () -> () {
    return { () ->() in
        print("Hello Ted!")
}
}
// 이런 식으로 리턴이 가능하다.


// 클로저는 직접 실행도 된다.
({ () -> () in
    print("Hello Ted!")
})()