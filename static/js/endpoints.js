// function to populate endpoint table

let GoatmenEndpoint = ("/api/v1.0/goatmen", "X", "")
let GoblinEndpoint = ("/api/v1.0/goblin", "X", "X")
let OgreEndpoint = ("/api/v1.0/ogre", "X", "")
let OrcEndpoint = ("/api/v1.0/orc", "X", "X")
let SkeletonEndpoint = ("/api/v1.0/skeleton", "X", "X")
let TrollEndpoint = ("/api/v1.0/troll", "X", "X")


let EndpointArray = (GoatmenEndpoint, GoblinEndpoint, OgreEndpoint, OrcEndpoint, SkeletonEndpoint, TrollEndpoint)



function populate_endpoint_array() {
    console.log(EndpointArray)
}

function populate_endpoint_table() {

}

document.onload(this, () => {
    populate_endpoint_array
})