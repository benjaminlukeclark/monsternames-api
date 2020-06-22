// function called to post to api to add new entry
function apiPost(e) {
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
  var lastNameValue = document.getElementById("firstNameInput").value
  var apiKey = document.getElementById("apiKeyInput").value
  // then attempt POST
  var result = ''
  if (endpointDict[selectedItem].firstName == true & firstNameValue.length > 0) {
    firstNameURL = endpointDict[selectedItem].url + 'firstName'
    firstNameData = {
      firstName : firstNameValue
    }
    createNewRecord(firstNameURL, firstNameData, apiKey)

  } else if (endpointDict[selectedItem].lastName == true & lastNameValue.length > 0) {
    lastNameURL = endpointDict[selectedItem].url + 'lastName'
    lastNameData = {
      lastName : lastNameValue
    }
    createNewRecord(lastNameURL, lastNameData, apiKey)
  }

 
}

function createNewRecord(url, data, apiKey) {
  postData(url, data, apiKey)
  .then(data => {
    console.log(data); // JSON data parsed by `response.json()` call
  });
}

// Example POST method implementation:
async function postData(url, data, apiKey) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers: {
      'Content-Type' : 'application/json',
      'x-api-key': apiKey
    },
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}