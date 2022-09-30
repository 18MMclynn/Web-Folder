let choice = prompt("Type: Add: Subtract: Divide: Multiply: "); 
if(choice == "Add"){
    let myFirstNumber = Number(prompt("Enter a 1st Number"));
    let mySecondNumber = Number(prompt("Enter a 2nd Number"));
    console.log("The Total Is: ", myFirstNumber + mySecondNumber)
}else if(choice == "Subtract"){
    let myFirstNumber = Number(prompt("Enter a 1st Number"));
    let mySecondNumber = Number(prompt("Enter a 2nd Number"));
    console.log("The Difference Is: ", myFirstNumber - mySecondNumber)
}else if(choice == "Divide"){
    let myFirstNumber = Number(prompt("Enter a 1st Number"));
    let mySecondNumber = Number(prompt("Enter a 2nd Number"));
    console.log("The Remainder Is: ", myFirstNumber / mySecondNumber)
}else if(choice == "Multiply"){
    let myFirstNumber = Number(prompt("Enter a 1st Number"));
    let mySecondNumber = Number(prompt("Enter a 2nd Number"));
    console.log("The Average Is: ", myFirstNumber * mySecondNumber)
}