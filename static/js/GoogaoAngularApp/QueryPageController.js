app.controller("queryPageCtrl", function($scope, $http, $location){
  $scope.search = function(e) {
    console.log("in function");
    e.preventDefault()
    $http({
      method : "POST",
      url : "/ajaxtest",
    }).then(function onSuccess(response){
      $location.path('/test')
      console.log(response.data.user)
    }, function onError(error) {
      console.log(error)
    });
  }
});
