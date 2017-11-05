app.config(function($routeProvider){
  $routeProvider
  .when("/", {
    templateUrl : "/static/js/GoogaoAngularApp/Templates/HomePage.html"
  })
  .when("/test", {
    templateUrl: "/static/js/GoogaoAngularApp/Templates/ResultsPage.html"
  });
});
