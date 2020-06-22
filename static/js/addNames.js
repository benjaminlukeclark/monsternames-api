// function called to post to api to add new entry
function apiPost(e) {
  // first we clear whatever data is already in the results column
  document.getElementById('apiPostResult').innerHTML = ''
  // then move on to actually doing things...

  // base url for post queries
  let baseUrl = 'https://monsternames-api.com/api/v1.0/'
  // create dict to hold verification info
  var endpointDict ={
    Goatmen : {
      firstName : true,
      lastName: false,
      base: baseUrl + 'goatmen/'
    },
    Goblin : {
      firstName : true,
      lastName: true,
      base: baseUrl + 'goblin/'
    },
    Ogre : {
      firstName : true,
      lastName: false,
      base: baseUrl + 'ogre/'
    },
    Orc : {
      firstName : true,
      lastName: true,
      base: baseUrl + 'orc/'
    },
    Skeleton : {
      firstName : true,
      lastName: true,
      base: baseUrl + 'skeleton/'
    },
    Troll : {
      firstName : true,
      lastName: true,
      base: baseUrl + 'troll/'
    }
  }
  // get current value of selected monsternames
  var selectedItem = document.getElementById("monsterSelect").value
  // and value of required items
  var firstNameValue = document.getElementById("firstNameInput").value
  var lastNameValue = document.getElementById("lastNameInput").value
  var apiKey = document.getElementById("apiKeyInput").value
  // then attempt POST
  var result = ''
  // attempt first name post
  if (endpointDict[selectedItem].firstName == true & firstNameValue.length > 0) {
    firstNameURL = endpointDict[selectedItem].base + 'firstName'
    firstNameData = "firstName=" + firstNameValue
    createNewRecord(firstNameURL, firstNameData, apiKey)

  }
  // attempt last name post
  if (endpointDict[selectedItem].lastName == true & lastNameValue.length > 0) {
    lastNameURL = endpointDict[selectedItem].base + 'lastName'
    lastNameData = "lastName=" + lastNameValue
    createNewRecord(lastNameURL, lastNameData, apiKey)
  }

  if ((firstNameValue.length + lastNameValue.length) == 0) {
    let errorDict = {"error" : "Unable to query API", "errorDetails" : {} }
    errorDict["errorDetails"] = {
      "exception" : 'NoValidInput',
      "message" : 'You must enter data into either the first or last name fields before clicking submit'
    }
    console.log(errorDict)
    let errorJson = JSON.stringify(errorDict, null, 4)
    document.getElementById("apiPostResult").innerHTML += errorJson
  }

 
}

function createNewRecord(url, data, apiKey) {
  postData(url, data, apiKey)
  .then(data => {
    let dataJson = JSON.stringify(data, null, 4)
    document.getElementById('apiPostResult').innerHTML += dataJson
  })
  .catch(function(err) {
    let errorDict = {"error" : "Unable to query API", "errorDetails" : {} }
    errorDict["errorDetails"] = {
      "exception" : err.name,
      "message" : err.message
    }
    console.log(errorDict)
    let errorJson = JSON.stringify(errorDict, null, 4)
    document.getElementById("apiPostResult").innerHTML += errorJson
    })
}

// Example POST method implementation:
async function postData(url, data, apiKey) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers: {
      'x-api-key': apiKey,
      'content-type' : 'application/x-www-form-urlencoded'
    },
    body: data // body data type must match "Content-Type" header
  })
  return response.json(); // parses JSON response into native JavaScript objects
}