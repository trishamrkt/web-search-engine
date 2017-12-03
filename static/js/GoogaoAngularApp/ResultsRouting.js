app.config(function($routeProvider){
  $routeProvider
  .when("/", {
    templateUrl : "/static/js/GoogaoAngularApp/Templates/HomePage.html"
  })
  .when("/results", {
    templateUrl: "/static/js/GoogaoAngularApp/Templates/ResultsPage.html"
  })
  .when("/history", {
    templateUrl: "/static/js/GoogaoAngularApp/Templates/HistoryTab.html"
  })
  .when("/images", {
    templateUrl: "/static/js/GoogaoAngularApp/Templates/ImagesTab.html"
  });
});
