// function called on home page to get example restapi output
function apiGet(e) {
    // get url from page
    var selectList = document.getElementById("endpointSelect");
    var url = selectList.options[selectList.selectedIndex].value;
    console.log(url)
    fetch(url)
    .then((resp) => resp.json()) // Transform the data into json
    .then(function(data) {
      let dataJson = JSON.stringify(data, null, 4)
      console.log(dataJson)

      var rowData = `
      <tr>
      <th scope="row">1</th>
      <td>Goatmen</td>
      <td>Fluffy</td>
      <td></td>
    </tr>
    `
      document.getElementById("apiGetResult").innerHTML = dataJson
      
      })
    .catch(function(err) {
      let errorDict = {"error" : "Unable to query API", "errorDetails" : {} }
      errorDict["errorDetails"] = {
        "exception" : err.name,
        "message" : err.message
      }
      console.log(errorDict)
      let errorJson = JSON.stringify(errorDict, null, 4)
      document.getElementById("apiGetResult").innerHTML = errorJson
    })

    return false // done to prevent reload of page
}

var getResultsTemplate = `
<table class="table" id="getResults">
<thead>
  <tr>
    <th scope="col">#</th>
    <th scope="col">Monster</th>
    <th scope="col">First name</th>
    <th scope="col">Last name</th>
  </tr>
</thead>
<tbody>
</tbody>
</table>
`;

function clearTable(e) {
  document.getElementById("getResults").innerHTML = getResultsTemplate

}