// function to populate endpoint table
let GoatmenEndpoint = ["/api/v1.0/goatmen", "X", ""]
let GoblinEndpoint = ["/api/v1.0/goblin", "X", "X"]
let OgreEndpoint = ["/api/v1.0/ogre", "X", ""]
let OrcEndpoint = ["/api/v1.0/orc", "X", "X"]
let SkeletonEndpoint = ["/api/v1.0/skeleton", "X", "X"]
let TrollEndpoint = ["/api/v1.0/troll", "X", "X"]


let EndpointArray = [GoatmenEndpoint, GoblinEndpoint, OgreEndpoint, OrcEndpoint, SkeletonEndpoint, TrollEndpoint]



function populate_endpoint_table() {

    for(let i = 0; i < EndpointArray.length; i++) {
        let endpointName = EndpointArray[i][0]
        let endpointFirstName = EndpointArray[i][1]
        let endpointLastName = EndpointArray[i][2]
        let newRow = `<tr><td>${endpointName}</td><td>${endpointFirstName}</td><td>${endpointLastName}</td></tr>`
        document.getElementById("endpointTBody").innerHTML += newRow
    }
}

window.onload = function() {
    populate_endpoint_table()
}