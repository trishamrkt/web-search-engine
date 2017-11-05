app.controller("queryPageCtrl", function($scope, $http, $location){
  $scope.search_results = []
  $scope.results_page_title = ""

  $scope.search = function(e) {
    console.log("in function");
    e.preventDefault()
    $http({
      method : "POST",
      url : "/ajaxtest",
    }).then(function onSuccess(response){
      // JSON object
      var data = response.data
      $scope.return_results(data);

      // Go to results page
      $location.path('/results')

      if ($scope.search_results.length !== 0){}
        $scope.results_page_title = "testing"
      }
      else {
        $scope.results_page_title = "sorry no results"
      }

    }, function onError(error) {
      console.log(error)
    });
  }

  // Function to place search results in search_results array
  $scope.return_results = function(data) {
    // Empty search_results in case there are results from prev searches
    $scope.search_results = []
    // Get number of elements in JSON array
    num_results = length(data);

    // Loop through all of the elements and place their objects in search_results array
    for (var i = 0; i < num_results; i++) {
      $scope.search_results.push(data[i])
    }
  }

  // Get length of an arbitrary object
  function length(obj) {
    return Object.keys(obj).length;
  }

});
