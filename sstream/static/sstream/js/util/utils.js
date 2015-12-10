/**
 * Created by shakti on 17/2/15.
 */


$("#img-list img").on('click', function(){
        $(this).toggleClass('active');
});

var convertToQueryParam = function(data) {

    var queryString = "";
    var counter = 0;

    var add = function(key, value) {
        return key + "=" + value;
    };

    var appendQuery = function(str) {
        if (counter !== 0) {
           queryString += "&"+str
        } else {
           queryString+=str
        }
    };

    jQuery.each(data, function(keyStr, val) {

        if (jQuery.isArray(val)) {
            var key = keyStr;
            jQuery.each(val, function(index, val) {
                appendQuery(add(key, val));
            } );
        }
        else {
            appendQuery(add(keyStr, val));
        }

        counter = counter + 1;

    });

    return queryString;
};
