/**
 * Created by shakti on 22/2/15.

 */

myApp.controller('Ctrl16', ['$scope','$http', '$filter', function($scope, $http, $filter) {

    $scope.nextLink = null;
    $scope.previousLink = null;
    $scope.currentPage = 1;
    $scope.totalItems = 1;
    $scope.prevPage = 0;
    $scope.itemsPerPage = 6;
    $scope.centers=[];
    $scope.imageStatus=["True","False"];
    $scope.daypassStatus=["True"];

    $scope.centerList = [];
    $scope.st_today = function() {
        $scope.st_dt = null;
    };
    $scope.ed_today = function() {
        $scope.ed_dt = null;
    };
    $scope.st_today();
    $scope.ed_today();
    $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
    $scope.format = $scope.formats[0];
    $scope.st_open = function($event) {
        $event.preventDefault();
        $event.stopPropagation();

        $scope.opened1 = true;
    };
    $scope.ed_open = function($event) {
        $event.preventDefault();
        $event.stopPropagation();

        $scope.opened = true;
    };

    $scope.init = function() {

        $http.get("/fitcenter/center/?format=json").success(
            function (resp) {
                $scope.currentPage = 1;
                $scope.totalItems = resp.count;
                $scope.centerList = resp.results;
                $scope.prevPage = $scope.currentPage;
                $scope.nextLink = resp.next;
                $scope.previousLink = resp.previous;
                //$scope.itemsPerPage = resp.results.length;
            }
        );

        $http.get("/fitcenter/data/states/").success(
            function (resp) {
                $scope.status_list = resp;
            }
        )
    };

    $scope.pageChanged = function() {
        var filterStr = $scope.buildFilter();

           $http.get("/fitcenter/center/?"+filterStr +"&q="+Math.random()+"&"+"page="+$scope.currentPage).success(
                function (resp) {
                    $scope.totalItems = resp.count;
                    $scope.centerList = resp.results;
                }
            );

    };
    //new_dt is for getting the next date of selected date
    $scope.buildFilter = function() {
        var fil = "?format=json";
        if ($scope.centers!=null && $scope.centers.length!=0) {
            fil = fil + "&" + "name="+$scope.centers.replace('&','%26');
        }
        if ($scope.st_dt != null && $scope.ed_dt != null) {
            var st_filter = $filter('date')($scope.st_dt, 'yyyy-MM-dd');
            fil = fil + "&" + "min_updated=" + st_filter;

            var ed_dt = new Date($scope.ed_dt);
            ed_dt.setDate(ed_dt.getDate() + 1);
            var ed_filter = $filter('date')(ed_dt, 'yyyy-MM-dd');
            fil = fil + "&" + "max_updated="+ed_filter;

        }
        if ($scope.st_dt != null && $scope.ed_dt == null) {
            st_filter = $filter('date')($scope.st_dt, 'yyyy-MM-dd');
            fil = fil + "&" + "min_updated=" +st_filter;
        }
        if ($scope.st_dt == null && $scope.ed_dt != null) {
            var ed_dt = new Date($scope.ed_dt);
            ed_dt.setDate(ed_dt.getDate() + 1);
            var ed_filter = $filter('date')(ed_dt, 'yyyy-MM-dd');
            fil = fil + "&" + "max_updated="+ed_filter;

        }
        if ($scope.status != null ) {
            fil = fil + "&" + "status="+$scope.status.name;
        }
        if ($scope.user != null) {

            fil = fil + "&" + "assigned="+$scope.user;
        }

        if ($scope.imageStatus != null) {
            fil = fil + "&" + "image_status="+$scope.image_status;
        }
        if ($scope.day_pass == 'True') {
            fil = fil + "&" + "day_pass=8";
        }


        return fil;
    };


    $scope.getUser = function(val) {
        return $http.get('/fitcenter/users/', {
            params: {
                search: val,
                sensor: false
            }
        }).then(function(response){
            return response.data;
        });
    };
    $scope.reset=function()
    {
        $scope.centers=null;
        $scope.ed_dt=null;
        $scope.st_dt=null;
        $scope.status=null;
        $scope.user=null;
        $scope.image_status=null;

        $scope.init($scope.centerId);
    }
       $scope.getCenters = function(val) {
        return $http.get('/fitcenter/center/all/', {
            params: {
                search: val
            }
        }).then(function(response){
           return  response.data;
        });
    };

    $scope.submitForm = function() {
        var filterStr = $scope.buildFilter();
        $scope.isProcessing = true;
        $http.get("/fitcenter/center/"+filterStr +"&q="+Math.random()).success(
            function (resp) {
                $scope.prevPage = $scope.currentPage;
                $scope.totalItems = resp.count;
                $scope.centerList = resp.results;
                $scope.nextLink = resp.next;
                $scope.previousLink = resp.previous;
                $scope.isProcessing = false;
                filterStr="";
                resp=null;
            }
        );

    }

}]);

myApp.controller('review_ctrl', ['$scope','$http', '$filter', function($scope, $http, $filter) {

    $scope.nextLink = null;
    $scope.previousLink = null;
    $scope.currentPage = 1;
    $scope.totalItems = 1;
    $scope.prevPage = 0;
    $scope.itemsPerPage = 6;
    $scope.centers=[];
    $scope.centerId=0;
    $scope.centerReviews = [];

    $scope.st_today = function() {
        $scope.st_dt = null;
    };
    $scope.ed_today = function() {
        $scope.ed_dt = null;
    };
    $scope.st_today();
    $scope.ed_today();
    $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
    $scope.format = $scope.formats[0];
    $scope.st_open = function($event) {
        $event.preventDefault();
        $event.stopPropagation();

        $scope.opened1 = true;
    };
    $scope.ed_open = function($event) {
        $event.preventDefault();
        $event.stopPropagation();

        $scope.opened = true;
    };

    $scope.init = function(center_id) {

        if(center_id!=null){
            $scope.centerId = center_id;
            $http.get("/fitcenter/center/" + $scope.centerId + "?format=json").success(
            function (resp) {
                $scope.centers = resp.name;
                $scope.submitForm();
            }
            ).error(function(data, status, header, config) {
                    $scope.successFlag = false;
                    $scope.msg = "Exception " + status + "!! " + data;
                });
        }

        $http.get("/fitcenter/center/reviews?format=json").success(
            function (resp) {
                $scope.currentPage = 1;
                $scope.totalItems = resp.count;
                $scope.centerReviews = resp.results;
                $scope.prevPage = $scope.currentPage;
                $scope.nextLink = resp.next;
                $scope.previousLink = resp.previous;
                //$scope.itemsPerPage = resp.results.length;
            }
        );

        $http.get("/fitcenter/reviews/status").success(
            function (resp) {
                $scope.status_list = resp;
            }
        )
    };

    $scope.pageChanged = function() {
        //var filterStr = $scope.buildFilter();
        console.log($scope.currentPage);
        var filterStr = $scope.buildFilter();

            $http.get("/fitcenter/center/reviews"+ filterStr + "&page="+$scope.currentPage).success(
                function (resp) {
                    $scope.totalItems = resp.count;
                    $scope.centerReviews = resp.results;
                }
            );

    };

    $scope.fbReditect = function(bt) {

            var fburl = "http://www.facebook.com/";
            var fetchurl = "/fitcenter/social/?format=json&provider=facebook&user_id="+bt;
            $http.get(fetchurl).success(function (resp) {
                $scope.successFlag = true;
                console.log(resp);
                fburl = fburl+resp[0].uid;
                window.open(fburl);




            }).error(function (data, status, headers, config) {
                $scope.successFlag = false;

                $scope.msg = "Some exception occurred! Please Try Again";

            });




    };


    $scope.buildFilter = function() {
        var fil = "?format=json";
        if ($scope.centers != null) {
            fil = fil + "&" + "center_name="+$scope.centers;
        }
        if ($scope.st_dt != null && $scope.ed_dt != null) {
            var st_filter = $filter('date')($scope.st_dt, 'yyyy-MM-dd');
            fil = fil + "&" + "min_updated=" + st_filter;

            var ed_filter = new Date($scope.ed_dt);
            ed_filter.setDate(ed_filter.getDate()+1);
            ed_filter = $filter('date')(ed_filter, 'yyyy-MM-dd');
            fil = fil + "&" + "max_updated=" +ed_filter;
        }
        if ($scope.st_dt != null && $scope.ed_dt == null) {
            st_filter = $filter('date')($scope.st_dt, 'yyyy-MM-dd');
            fil = fil + "&" + "min_updated=" +st_filter;

            //ed_filter = $filter('date')(new Date(), 'yyyy-MM-dd');
            //fil = fil + "&" + "max_updated=" +ed_filter;
        }
        if ($scope.st_dt == null && $scope.ed_dt != null) {
            ed_filter = new Date($scope.ed_dt);
            ed_filter.setDate(ed_filter.getDate()+1);
            ed_filter = $filter('date')(ed_filter, 'yyyy-MM-dd');
            fil = fil + "&" + "max_updated=" +ed_filter;
            //fil = fil + "&" + "min_updated=" +ed_filter;
        }
        if ($scope.status != null) {
            fil = fil + "&" + "status="+$scope.status.name;
        }

        return fil;
    };


    $scope.getUser = function(val) {
        return $http.get('/fitcenter/users/', {
            params: {
                search: val,
                sensor: false
            }
        }).then(function(response){
            return response.data;
        });
    };

       $scope.getCenters = function(val) {
        return $http.get('/fitcenter/center/all/', {
            params: {
                search: val
            }
        }).then(function(response){
           return  response.data;
        });
    };

    $scope.submitForm = function() {

        var filterStr = $scope.buildFilter();
        $scope.isProcessing = true;
        $http.get("/fitcenter/center/reviews"+filterStr +"&q="+Math.random()).success(
            function (resp) {
                $scope.prevPage = $scope.currentPage;
                $scope.totalItems = resp.count;
                $scope.centerReviews = resp.results;
                $scope.nextLink = resp.next;
                $scope.previousLink = resp.previous;
                $scope.isProcessing = false;
                filterStr="";
                resp=null;
                //$scope.itemsPerPage = resp.results.length;
            }
        );

    };

    $scope.deleteReview = function (review_id) {
        var x=window.confirm("Are you sure you want to delete this review?")
        if(x) {
            if (review_id != null) {
            $scope.review_id = review_id;
            }
            $scope.submitted = true;
            var param = {"review_id": $scope.review_id, "status_request": 5};
            $http({
                url : "/fitcenter/review/edit/",
                method : 'POST',
                data: $.param(param),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                    //'sessionid': $cookies.sessionid
                }

            }).success(function (data, status, header, config) {
                $scope.successFlag = true;
                $scope.msg = "Review deleted Successfully";
                setTimeout(function () { // wait and reload
                   window.location.reload(true);
                }, 10);
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
    };

    $scope.verifyReview = function (review_id) {
        var x=window.confirm("Are you sure you want to verify & publish this review?")
        if(x) {
            if (review_id != null) {
            $scope.review_id = review_id;
            }

            $scope.submitted = true;
            var param = {"review_id": $scope.review_id, "status_request": 3};
            $http({
                url : "/fitcenter/review/edit/",
                method : 'POST',
                data: $.param(param),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                    //'sessionid': $cookies.sessionid
                }

            }).success(function (data, status, header, config) {
                $scope.successFlag = true;
                $scope.msg = "Review verified & published Successfully";
                setTimeout(function () { // wait 3 seconds and reload
                   window.location.reload(true);
                }, 50);
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
    };

}]);