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

myApp.directive('dynamicUrl', function () {
    return {
        restrict: 'A',
        link: function postLink(scope, element, attr) {
            element.attr('src', attr.dynamicUrlSrc);
        }
    };
});

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
    $scope.length = 0;
    $scope.mediaType = 0;
    $scope.description = "";
    $scope.fileTitle = "";
    $scope.theme = "";
    $scope.language = "";
    $scope.seriesTitle = "";
    $scope.seriesNumber = "";
    $scope.contentType = "";
    $scope.artist = "";
    $scope.category = "";
    $scope.categoryList = [];
    $scope.themesList = [];
    $scope.contentTypeList = [];
    $scope.tags = "";
    $scope.monetize = false;
    $scope.premiumRequired = false;
    $scope.loginRequired = false;
    $scope.mediaTypeList = [];
    $scope.entity = "";
    $scope.create_dt = "";

     $scope.clickMeMonetize = function(param) {
        if (param) {
            $scope.monetize = false;
        } else {
            $scope.monetize = true;
        }
    };


    $scope.setValues = function (meta_id) {
        $scope.meta_id = meta_id;
        $http.get("/video/"+meta_id).success(
            function (resp) {
                $scope.video_url= resp;
            });

         $http.get("/ssadmin/mediatype/all/").success(
            function (resp) {
                $scope.mediaTypeList= resp;
            });

              $http.get("/ssadmin/contenttype/all/").success(
            function (resp) {
                $scope.contentTypeList= resp;
            });


                 $http.get("/ssadmin/category/all/").success(
            function (resp) {
                $scope.categoryList= resp;
            });

                $http.get("/ssadmin/themes/all/").success(
            function (resp) {
                $scope.themesList= resp;
            });



        $http.get("/metadata/exists/" + $scope.meta_id).success(
            function (resp) {
                $scope.edit = resp;
                if ($scope.edit) {
                    $http.get("/get/metadata/" + $scope.meta_id).success(
                        function (resp1) {
                            $scope.length = resp1.length;
                            $scope.mediaType = resp1.mediaType;
                            $scope.description = resp1.description;
                            $scope.fileTitle = resp1.fileTitle;
                            $scope.theme = resp1.themes;
                            $scope.language = resp1.language;
                            $scope.seriesTitle = resp1.seriesTitle;
                            $scope.seriesNumber = resp1.seriesNumber;
                            $scope.contentType = resp1.contentType;
                            $scope.artist = resp1.artist;
                            $scope.category= resp1.category;
                            $scope.tags = resp1.tags;
                            $scope.monetize = resp1.monetize;
                            $scope.premiumRequired = resp1.premium_required;
                            $scope.loginRequired = resp1.login_required;
                            $scope.entity = resp1.entity;
                            $scope.create_dt = resp1.create_dt;

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
                'description': $scope.description,'fileTitle':$scope.fileTitle,
                'theme' : $scope.theme, 'language' : $scope.language , 'seriesTitle' : $scope.seriesTitle ,
                'seriesNumber' : $scope.seriesNumber , 'contentType' : $scope.contentType , 'artist' : $scope.artist,
                'category' : $scope.category , 'tags' : $scope.tags ,  'monetize' :$scope.monetize ,'create_dt' :$scope.create_dt,
                'premiumRequired' : $scope.premiumRequired , 'loginRequired' : $scope.loginRequired , 'entity' :$scope.entity
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


