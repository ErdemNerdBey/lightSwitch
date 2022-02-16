document.body.style.backgroundColor = "black";

function achtergrondVeranderen() {
    if (document.body.style.backgroundColor == "yellow") {
        document.body.style.backgroundColor = "black";
        console.log("licht is uit :(");
        lichtKnop.innerText = "light is uit";
    } else{
        document.body.style.backgroundColor = "yellow";
        console.log("licht is aan!!! :)");
        lichtKnop.innerText = "light is aan";
    }
}  