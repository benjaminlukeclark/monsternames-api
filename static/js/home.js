// function called on home page to get example restapi output
function apiGet() {
    // get url from page
    let url = document.getElementById('endpoint').innerHTML
    console.log(url)
    fetch(url)
    .then((resp) => resp.json()) // Transform the data into json
    .then(function(data) {
      let dataJson = JSON.stringify(data, null, 4)
      document.getElementById("apiGETResult").innerHTML = dataJson
      })
    .catch(function(err) {
      let errorDict = {"error" : "Unable to query API", "errorDetails" : {} }
      errorDict["errorDetails"] = {
        "exception" : err.name,
        "message" : err.message
      }
      console.log(errorDict)
      let errorJson = JSON.stringify(errorDict, null, 4)
      document.getElementById("apiGETResult").innerHTML = errorJson
    })

    return false // done to prevent reload of page
}

window.onload = function() {
  document.getElementById("apiGET").onclick = apiGet()
}