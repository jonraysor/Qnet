  // Set the configuration for your app
  // TODO: Replace with your project's config object
/*
  var config = {
    apiKey: "AIzaSyCGu-35PaXaoIXyxhZPHz_nDwZ5BHn0t44",
    authDomain: "pqnet-62c3e.firebaseapp.com",
    databaseURL: "https://qnet-62c3e.firebaseio.com",
    storageBucket: "bucket.appspot.com"
  };
  firebase.initializeApp(config);

  // Get a reference to the database service
  var database = firebase.database();

  console.log(database)


  */
  async function loadJson(url) {
  return new Promise(function (resolve, reject) {
    let xhr = new XMLHttpRequest()
    xhr.overrideMimeType('application/json')
    xhr.open('GET', url, true)
    xhr.onload = function () {
      if (this.status >= 200 && this.status < 300) {
        resolve(xhr.response)
      } else {
        reject({
          status: this.status,
          statusText: xhr.statusText
        })
      }
    }
    xhr.onerror = function () {
      reject({
        status: this.status,
        statusText: xhr.statusText
      })
    }
    xhr.send()
  })
}

async function initDropdowns() {
  let json = await loadJson('school.json')
  let data = JSON.parse(json)
  this.data = data
  setSchoolsDropdown()
  enableDropdown('schools')
}
