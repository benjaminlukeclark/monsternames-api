// function called on home page to get example restapi output
function apiGet() {
    // get url from page
    let url = document.getElementById('endpoint').innerHTML
    fetch(url)
    .then((resp) => resp.json()) // Transform the data into json
    .then(function(data) {
      console.log(data)
      })
    .catch(function(err) {

    })

    return false // done to prevent reload of page
}