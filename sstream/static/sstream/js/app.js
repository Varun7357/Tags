'use strict';

var myApp = angular.module('app',['ngCookies', 'checklist-model','angucomplete',
        'ui.bootstrap', 'ngMap', 'GoogleDirectives', 'lr.upload', 'ngAnimate', 'ngLoadingSpinner'])
    .config([ '$interpolateProvider', '$httpProvider',
        function($interpolateProvider, $httpProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
            //$httpProvider.default.withCredentials = true;
        }])
    .run(['$http', '$cookies',
        function($http, $cookies){
            $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
            $http.defaults.withCredentials = true
        }
    ]);


//// get list of center types and create a service center
//myApp.controller('gymController', ['$scope','$http', function($scope, $http){
//
//    $scope.edit = false;
//    $scope.males = 0;
//    $scope.females = 0;
//    $scope.trainers = 0;
//    $scope.spotters = 0;
//    $scope.website = "";
//    $scope.about = "";
//
//    $scope.setZero= function(sex){
//      if(sex=='M'){
//          $scope.females=0;
//      }
//        else{
//          $scope.males=0;
//      }
//    };
//
//
//    $scope.init = function(center_id) {
//
//        if (center_id != null) {
//            $scope.edit = true;
//            $scope.centerId = center_id;
//        }
//
//        $http.get("/fitcenter/center/types").success(
//            function(response) {
//            $scope.centerList = response;
//            }
//        );
//
//        if ($scope.edit) {
//            $http.get("/fitcenter/center/"+ $scope.centerId +"/?format=json").success(
//                function (resp) {
//                    $scope.name = resp.name;
//                    $scope.sex = resp.sex;
//                    $scope.service_type = resp.centerType.id;
//                    $scope.website = resp.website;
//                    $scope.males = resp.males;
//                    $scope.females = resp.females;
//                    $scope.trainers = resp.trainers;
//                    $scope.spotters = resp.spotters;
//                    $scope.about = resp.aboutfitcenter.content;
//                }
//            );
//        }
//    };
//
//    $scope.submitForm = function () {
//        $scope.submitted = true;
//        if ($scope.gymForm.$valid) {
//            //alert("Form is valid!");
//
//            var params = {'name':$scope.name , 'sex':$scope.sex,
//                'center_type': $scope.service_type, 'website':$scope.website, 'males':$scope.males,
//                'females' : $scope.females, 'trainers': $scope.trainers, 'spotters': $scope.spotters, 'about':$scope.about };
//
//            var api_url = "/fitcenter/create/";
//
//
//            if ($scope.edit) {
//                // call Edit API
//                params.id = $scope.centerId;
//                api_url = "/fitcenter/edit/"
//
//            }
//            $http({
//                url : api_url,
//                method : 'POST',
//                data: $.param(params),
//                headers: {
//                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
//                    //'sessionid': $cookies.sessionid
//                }
//            }).success(function(data, status, header, config) {
//                $scope.successFlag = true;
//                if (!$scope.edit) {
//                    $scope.centerId = data.id;
//                    $scope.msg = "Service Center Created Successfully";
//                } else {
//                    $scope.msg = "Service Center edited Successfully";
//                }
//
//            }).error(function(data, status, header, config) {
//                     $scope.successFlag = false;
//                if (status == 403) {
//                    $scope.msg = "Access denied";
//                }
//                else {
//                $scope.msg = "Some exception occurred! Please Try Again";
//            }
//            });
//        }
//        else {
//            $scope.successFlag = false;
//            $scope.msg = "Some exception occurred! Please Try Again";
//        }
//    };
//
//
//}]);




