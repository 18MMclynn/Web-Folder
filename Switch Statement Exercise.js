//1.
let x = Math.floor(Math.random() *3)+1;

/*
Math.random() generates a number greater than or equal to 0 and less than 1. If we 
multiply this by 3 we get a number between 0 and less than 3. 
When we take Math.floor() of our result we get a number 0,1 or2 and adding 1 to our 
answer gives us a number between 1 and 3. 
*/

/*
Use a switch statement and the random number to assign rock, paper or scissors to the 
computer variable and then use and if statement to see who has won. 
*/

let myVar = 'Rock'

switch(myVAR){
case 'Rock':
console.log("Rock");
break;
case 'Paper':
console.log("Paper");
break;
case 'Scissors':
console.log("Scissors");
default:
console.log("Error");

}









//3.
let myVar = 'A+'

switch(myVAR){
case 'A+':
console.log("You got a H1");
break;
case 'F-':
console.log("you got a H8");
break;
default:
console.log("Grade not recognized");

}
