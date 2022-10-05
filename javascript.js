console.log("Hello")
let k = 5;

console.log(k--);

console.log(k)

console.log(--k)

console.log(5 == 3);

console.log(4 ==4);

console.log(5!=4);
console.log(4!=4);

console.log( 5> 4);

console.log(4 >5);

console.log(5< 4);
console.log(4<5);

console.log( 5<= 4);

console.log(4 <=5);

let n = 12;

n+= 12; // Equal to n = + 12
console.log(n)

n -= 4; // Equal to n = n- 4
console.log(n);

n *= 5; // Equal to n = n *5
console.log(n);


let y = 4;

y/= 2; // Equal to y = y/2
console.log(y);

y %= 2; // Equal to y = y%2
console.log(y)

let first = 10;

let second = 12;

console.log(first>second?"True":"False");

let myString = "Hello";

let myNumber = 12;

console.log(typeof(myNumber));

//Prompt Function is used for user input, default data is a string, To convert input to number, wrap the prompt in a NUMBER() function call

let mySecondString = prompt("Enter something");

console.log(mySecondString);

let mySecondNumber = Number(prompt("Enter a Number"));
console.log(mySecondString);

let myage = 400;

if (myage > 500);{
console.log("you are over 500 years old");

}



if (myage > 500){
console.log("you are over 500 years old");
}else{
console.log("you are over 500 years old");
}

if (myage > 500){
console.log("you are over 500 years old");
}else if(myage<500){
console.log("you are over 500 years old");
}else{
console.log("you must be 500 years old");
}



/*
Logical Operators
These test for "true" and "false" conditions
*/

/*
LOGICAL AND (&&)
RETURNS TRUE IF BOTH OPERATORS ARE TRUE
*/

let a = true;
let b = true;
console.log(a && b); //Will print true to the console
// as BOTH a and b are true

b = flase;
console.log(a && b); //Will print false to the console
// as a and b are not BOTH true


let firstNumber = 10;
let secondNumber = 20;

if((firstNumber >5) && (secondNumber > 15)){
    console.log("first is greater than 5 and second than 15");
}else{
    console.log("One of the expressions failed the test");
}


if(firstNumber >secondNumber){
console.log("line 1: first is lesser");
console.log("line 2: first is lesser");
}else{

}

/*
LOGICAL OR (||) - IF EITHER A OR B IS TRUE IT IS ALL TRUE
*/

a = true;
b = true;

console.log(a || b);


/*
LOGICAL NOT (!) - REVERSES THE RESULT IF TRUE BECOMES FALSE
IF FALSE BECOMES TRUE
*/

console.log(!(a)); 







/*
SWITCH STATEMENT
*/

let myVar = 'A'

switch(myVAR){
case 'A':
console.log("You got a A");
break;
case 'B':
console.log("you got a B");
break;
default:
console.log("Grade not recognized");

}