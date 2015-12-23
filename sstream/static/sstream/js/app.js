'use strict';

var myApp = angular.module('app', ['ngCookies', 'angucomplete', 'angularSpinner',
    'ui.bootstrap', 'ngMap', 'lr.upload', 'ngAnimate', 'ngLoadingSpinner'])
    .config(['$interpolateProvider', '$httpProvider',
        function ($interpolateProvider, $routeProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
        }])
    .run(['$http', '$cookies',
        function ($http, $cookies) {
            $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
            $http.defaults.withCredentials = true
        }
    ]);


myApp.controller('searchController', ['$scope', '$http', '$filter', function ($scope, $http, $filter) {

    $scope.nextLink = null;
    $scope.previousLink = null;
    $scope.currentPage = 1;
    $scope.totalItems = 0;
    $scope.prevPage = 0;
    $scope.itemsPerPage = 6;
    $scope.metaFiles = [];
    $scope.companies = [];
    $scope.selectedCompany = [];


    $scope.getCompanies = function (val) {
        return $http.get('/ssadmin/company/all/', {
            params: {
                search: val
            }
        }).then(function (response) {
            $scope.companies = response.data;
            return response.data;

        });
    };


    $scope.st_open = function ($event) {
        $event.preventDefault();
        $event.stopPropagation();

        $scope.opened1 = true;
    };
    $scope.ed_open = function ($event) {
        $event.preventDefault();
        $event.stopPropagation();

        $scope.opened = true;
    };
    //
    //$scope.init = function() {
    //
    //    $http.get("/ssadmin/metastatus/all/").success(
    //        function (resp) {
    //            $scope.status_list = resp;
    //        }
    //    )
    //};

    $scope.pageChanged = function () {
        var filterStr = $scope.buildFilter();

        $http.get("metafiles?" + filterStr + "&" + "page=" + $scope.currentPage).success(
            function (resp) {
                $scope.totalItems = resp.count;
                $scope.centerList = resp.results;
            }
        );

    };
    //new_dt is for getting the next date of selected date
    $scope.buildFilter = function () {
        var fil = "?format=json";
        if ($scope.companies != null && $scope.companies.length != 0) {
            fil = fil + "&" + "name=" + $scope.selectedCompany;
        }
        //if ($scope.status != null ) {
        //    fil = fil + "&" + "status="+$scope.status.name;
        //}

        return fil;
    };


    $scope.reset = function () {
        $scope.companies = null;
        //$scope.status=null;

    };


    $scope.submitForm = function () {
        var filterStr = $scope.buildFilter();
        $scope.isProcessing = true;
        $http.get("/ssadmin/metafiles" + filterStr).success(
            function (resp) {

                $scope.prevPage = $scope.currentPage;
                $scope.totalItems = resp.count;
                $scope.metaFiles = resp.results;
                $scope.nextLink = resp.next;
                $scope.previousLink = resp.previous;
                $scope.isProcessing = false;
                filterStr = "";
                resp = null;
            }
        );

    }

}]);

/* Directives */
angular.module('GoogleDirectives', []).
    directive('googlePlaces', function () {
        return {
            restrict: 'E',
            replace: true,
            // transclude:true,
            scope: {location: '='},
            template: '<input class="form-control" type="text" id="google_places_ac" name="google_places_ac">',
            link: function ($scope, elm, attrs) {
                var autocomplete = new google.maps.places.Autocomplete($("#google_places_ac")[0], {});
                google.maps.event.addListener(autocomplete, 'place_changed', function () {
                    var place = autocomplete.getPlace();
                    $scope.location = place; //place.geometry.location.lat() + ',' + place.geometry.location.lng();
                    $scope.lat = place.geometry.location.A;
                    $scope.long = place.geometry.location.F;
                    $scope.locality_name = $scope.location.name;
                    //$scope.place = place;
                    $scope.$apply();
                });
            }
        }
    });

myApp.controller('metaFieldController', ['$scope', '$http', function ($scope, $http, $location) {

    $scope.edit = false;
    $scope.length = "";
    $scope.version = "";
    $scope.mediaType = "";


    $scope.setValues = function (meta_id) {

        $scope.meta_id = meta_id;
        $http.get("/metadata/exists/" + $scope.meta_id).success(
            function (resp) {
                $scope.edit = resp;
                if ($scope.edit) {
                    $http.get("/get/metadata/" + $scope.meta_id).success(
                        function (resp) {
                            $scope.length = resp.length;
                            $scope.mediaType = resp.mediaType;
                            $scope.version = resp.version;
                        }
                    );
                }

            });


    };

    $scope.submitForm = function () {
        $scope.submitted = true;
        if ($scope.metaForm.$valid) {

            var params = {
                'length': $scope.length, 'mediaType': $scope.mediaType,
                'version': $scope.version
            };

            var api_url = "/save/meta/" + $scope.meta_id;

            $http({
                url: api_url,
                method: 'POST',
                data: $.param(params),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                    //'sessionid': $cookies.sessionid
                }
            }).success(function (data, status, header, config) {
                $scope.successFlag = true;
                if (!$scope.edit) {
                    $scope.field_id = data.id;
                    $scope.msg = "Saved Successfully";
                } else {
                    $scope.msg = " Edited Successfully";
                }

            }).error(function (data, status, header, config) {
                $scope.successFlag = false;
                if (status == 403) {
                    $scope.msg = "Access denied";
                }
                else {
                    $scope.msg = "Some exception occurred! Please Try Again";
                }
            });
        }
        else {
            $scope.successFlag = false;
            $scope.msg = "Some exception occurred! Please Try Again";
        }
    };


}]);


