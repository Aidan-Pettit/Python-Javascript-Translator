// This will turn into "console.log"
console.log('Welcome!')

// And these variables will be prefixed with "let"
let num1 = 1
let num2 = 2

// Arithmetic operations are basically the same
let sum = num1 + num2

// Brackets are added around if statements
if (sum == 3) {
    console.log('The sum is 3!')
}

// Have you noticed that the comments changed too?
// "#" turned into "//"

// Additionally, some other keywords are different
// True -> true
true
// False -> false
false
// None -> null
null
// and -> &&
num1 < num2 && sum == 3
// or -> ||
num1 < num2 || sum == 3

// Finally, loops and functions (as well as if statements) have curly
// braces placed around them.

let list = [1, 2, 3]

for (let item of list) {
    console.log(item)
}

let counter = 0

while (counter <= 10) {
    console.log(counter)
    counter += 1
}


function greet(name) {
    console.log('Hello, my name is ', name)
}


// And that's it! Thank you for looking at this transator!
console.log('Thank you so much!')

// Don't forget to try running the new file with node!
