class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }

    sayHello() {
        console.log('Hello, my name is ', this.name)
    }
}

aidan = Person('Aidan', 18)

