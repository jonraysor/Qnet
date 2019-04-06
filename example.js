  // Set the configuration for your app
  // TODO: Replace with your project's config object
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