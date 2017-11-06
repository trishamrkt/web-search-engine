app.controller("queryPageCtrl", function($scope, $http, $location){
  $scope.search_results = []
  $scope.page_number = 0;
  $scope.results_page_title = ""

  $scope.search = function(e, query_string) {
    console.log("in function");
    console.log(query_string)
    e.preventDefault()
    $http({
      method : "POST",
      url : "/ajaxtest",
      data : { "keywords" : query_string}
    }).then(function onSuccess(response){
      // JSON object
      var data = response.data
      $scope.return_results(data);

      // Go to results page
      $location.path('/results')

      if ($scope.search_results.length !== 0){
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
    $scope.page_number = 0;

    // Get number of elements in JSON array
    var num_results = length(data);
    var num_pages = Math.ceil(num_results/5.0)

    // Keeps track of # of results - used to obtain 5 results per page
    var result_count = 0;
    var results_per_page = []

    // Loop through all of the elements and place their objects in search_results array
    for (var i = 0; i < num_results; i++) {
      if (result_count < 5){
        results_per_page.push(data[i])
        result_count += 1;
      }
      else {
        $scope.search_results.push(results_per_page)
        results_per_page = [data[i]]
        result_count = 0;
      }
    }

    if ($scope.search_results.length < num_pages)
      $scope.search_results.push(results_per_page)
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

  // Get length of an arbitrary object
  function length(obj) {
    return Object.keys(obj).length;
  }

});
