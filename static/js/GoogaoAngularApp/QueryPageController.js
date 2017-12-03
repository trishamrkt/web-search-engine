app.controller("queryPageCtrl", function($scope, $http, $location){
  $scope.search_results = []
  $scope.page_number = 0;
  $scope.results_page_title = ""
  $scope.no_results = false;
  $scope.login_display = false;
  $scope.login_success = true;
  $scope.user_name = "Sign in";
  $scope.login_submit = "Login"
  $scope.no_account = true;
  $scope.request_time = 0;
  $scope.signed_in = false;
  $scope.most_popular = [];
  $scope.history = [];


  $scope.googao_form_submit = function(e, username) {
    if ($scope.login_submit === "Login") {
      $scope.googaoLogin(e, username, "/googaoLogin")
    }
    else {
      $scope.googaoLogin(e, username, "/googaoSignup")
    }
  }

  $scope.googaoLogin = function(e, username, req_url) {
	  console.log("Googao Login Time Baby");
	  e.preventDefault();

	  $http({
		  method : "POST",
	      url : req_url,
	      data : { "username" : username}

	  }).then(function onSuccess(response){
		  var data = response.data;
		  if (data.success == true) {
			  $scope.close_login();
			  $scope.user_name = username;
        $scope.signed_in = true;
		  } else {
			  $scope.login_success = false;
		  }

	  });
  }

  $scope.search = function(e, query_string) {
    console.log("in function");
    console.log("fuck this");
    console.log($scope.signed_in)
    e.preventDefault();
    var start = performance.now();
    $http({
      method : "POST",
      url : "/query",
      data : { "keywords" : query_string}
    }).then(function onSuccess(response){

      var end = performance.now();
      $scope.request_time = end - start;
      console.log($scope.request_time);


      // JSON object
      var data = response.data
      $scope.return_results(data);

      // Go to results page
      $location.path('/results')

      if ($scope.search_results.length !== 0){
        $scope.no_results = false;
      }
      else {
        $scope.no_results = true;
      }

    }, function onError(error) {
      console.log(error)
    });
  }


  // Function to place search results in search_results array
  $scope.return_results = function(data) {
    // Empty search_results in case there are results from prev searches
    $scope.search_results = []
    $scope.page_number = 0;

    for (var i = 0; i < data.length; i++) {
      $scope.search_results.push(data[i])
    }
  }

  $scope.next_page = function() {
    if ($scope.page_number < $scope.search_results.length - 1)
      $scope.page_number += 1
  }

  $scope.prev_page = function() {
    if ($scope.page_number > 0)
      $scope.page_number -= 1
  }

  $scope.go_to_page = function(index) {
    $scope.page_number = index;
  }

  $scope.switch_tabs = function(link) {
    $location.path(link);
  }

  $scope.display_history = function() {
    $scope.switch_tabs('/history');

    $http({
      method: "POST",
      url: "/gethistory",
      data: {"username" : $scope.user_name }
    }).then(function onSuccess(response) {
      var data = response.data
      $scope.most_popular = data[0];
      $scope.history = data[1];
    })
  }

  $scope.login = function() {
    $scope.login_submit = "Login";
    $scope.login_display = true;
    $scope.no_account = true;
  }

  $scope.signup = function() {
    $scope.no_account = false;
    $scope.login_submit = "Sign up";
  }

  $scope.signout = function() {
    $scope.signed_in = false;
  }

  $scope.close_login = function() {
    $scope.login_display = false;
  }


  // Get length of an arbitrary object
  function length(obj) {
    return Object.keys(obj).length;
  }

});
