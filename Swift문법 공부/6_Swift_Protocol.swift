/// 프로토콜(Protocols)

> 상속 방향과 프로토콜의 필요성
> 

/// 프로토콜의 요구사항의 종류

- 최소한의 요구사항 나열
- 여러개의 프로토콜  구현  가능
- 프로토콜을 채택하려는 클래스, 구조체, 열거형에 최소한 이런 내용을 구현해야한다고 선언하는 부분
    - 속성 요구사항
    - 메서드 요구사항 (메서드/생성자/서브스크립트)

### 속성의 요구사항 정의하는 방법

- 속성의 뜻에서 var로 선언 (let으로 선언할 수 없음)
- get, set 키워드를 통해서 읽기/쓰기 여부를 설정 (최소한의 요구사항일뿐)
- 저장 속성/계산 속성으로 모두 구현 가능


protocol RemoteMouse {
    
    var id: String { get }                // ===> let 저장속성 / var 저장속성 / 읽기계산속성 / 읽기,쓰기 계산속성
    
    var name: String { get set }          // ===> var 저장속성 / 읽기,쓰기 계산속성

    static var type: String { get set }   // ===> 타입 저장 속성 (static)
                                          // ===> 타입 계산 속성 (class)
}


// 채택하면, (최소한의)요구사항을 정확하게 따라서 구현해야함

// 인스턴스 저장/계산 속성 =========================

struct TV: RemoteMouse {
    
    var id: String = "456"
    
    var name: String = "삼성티비"
    
    static var type: String = "리모콘"
}


let myTV = TV()
myTV.id
myTV.name
TV.type


## 메서드의 요구사항 정의하는 방법

### 프로토콜 메서드 요구사항

- 메서드의 헤드부분(인풋/아웃풋)의 형태만 요구사항으로 정의
- mutating 키워드: (구조체로 제한하는 것은 아님) 구조체에서 저장 속성 변경하는 경우,
    - 구조체도 채택 가능하도록 허락하는 키워드
- 타입 메서드로 제한 하려면, static키워드만 붙이면 됨
    - (채택해서 구현하는 쪽에서 static / class 키워드 모두 사용 가능)


    // 1) 정의
protocol RandomNumber {
    static func reset()         // 최소한 타입 메서드가 되야함 (class로 구현해서 재정의를 허용하는 것도 가능)
    func random() -> Int
    mutating func doSomething()
}


// 2) 채택 / 3) 구현
class Number: RandomNumber {
    
    static func reset() {
        print("다시 셋팅")
    }
    
    func random() -> Int {
        return Int.random(in: 1...100)
    }
    
    func doSomething() {
        print("놀고 있다 ")
    }
}


let n = Number()
n.random()
n.doSomething()
Number.reset()

// 1) 정의
protocol Togglable {
    mutating func toggle()        // mutating의 키워드는 메서드 내에서 속성 변경의 의미일뿐(클래스에서 사용 가능)
}


// 2) 채택 / 3) 구현
enum OnOffSwitch: Togglable {
    case on
    case off
    
    mutating func toggle() {
        switch self {   // .on   .off
        case .off:
            self = .on
        case .on:
            self = .off
        }
    }
}


var s = OnOffSwitch.off
s.toggle()
s.toggle()


class BigSwitch: Togglable {
    var isOn = false
    
    func toggle() {      // mutating 키워드 필요없음 (클래스 이기 때문)
        isOn = isOn ? false : true
    }
}


var big = BigSwitch()
print(big.isOn)
big.toggle()
print(big.isOn)

## 메서드 요구사항 - 생성자 요구사항

### 생성자 요구사항  (❗️실제 프로젝트에서 사용하는 경우 드뭄)

- 클래스는 (상속 고려해야함) 생성자 앞에 required를 붙여야함 (하위에서 구현을 강제)
구조체의 경우 상속이 없기 때문에, required 키워드 필요 없음
- 아니면 final을 붙여서 상속을 막으면 required 생략가능
- 클래스에서는 반드시 지정생성자로 구현할 필요없음(편의생성자로 구현도 가능)

class SomeClass: SomeProtocol {
    required init(num: Int) {
        // 실제 구현
    }
}

class SomeSubClass: SomeClass {
    // 하위 클래스에서 생성자 구현 안하면 필수 생성자는 자동 상속
    // required init(num: Int)
    
}



// 예제 - 2 ======================

protocol AProtocol {
    init()
}

class ASuperClass {
    init() {
        // 생성자의 내용 구현
    }
}

class ASubClass: ASuperClass, AProtocol {
    // AProtocol을 채택함으로 "required" 키워드 필요하고, 상속으로 인한 "override(재정의)" 재정의 키워드도 필요
    required override init() {
        // 생성자의 내용 구현
    }
}