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


//2.


let userchoice = prompt("Type: Rock, Paper, or Scissors");

let computerguess = '';

switch(x){
case 1:
computureguess = "Rock"
console.log("Rock");
break;
case 2:
computureguess = "Paper"
console.log("Paper");
break;
case 3:
computureguess = "Scissors"
console.log("Scissors");
default:
console.log("Error");

}


if (userchoice == computureguess){
console.log("Draw")
}else if(computureguess == "Rock" && userchoice == "Scissors"){
console.log("Computure Rock beats User Scisssors")
}else if(computureguess == "Scissors" && userchoice == "Rock"){
console.log("User Rock beats Computure Scisssors")
}else if(computureguess == "Paper" && userchoice == "Rock"){
console.log("Computure Paper beats User Rock")
}else if(computureguess == "Rock" && userchoice == "Paper"){
console.log("User Paper beats Computure Rock")
}else if(computureguess == "Scissors" && userchoice == "Paper"){
console.log("Computure Scissors beats User Paper")
}else if(computureguess == "Paper" && userchoice == "Scissors"){
console.log("User Scissors beats Computure Paper")
}
    
    






//3.

let levelchoice = prompt("Type: HigherLevel or OridinaryLevel");

let gradechoice = prompt("Type: H1-H8");

switch(x){
case 1:
gradechoice = "OrdinaryLevel"
console.log("H1-H8");
break;
case 2:
gradechoice = "HigherLevel"
console.log("H1-H8");
break;
default:
console.log("Grade Not Recgonized");

}
