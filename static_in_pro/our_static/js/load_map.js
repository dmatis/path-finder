/**
 * Created by hannahpark on 15-11-13.
 */

var map;
var markers = [];
var lastInputtedCoordinate;
var allCoordinates = [];
var tempAllCoordinates = [];
var polylines = [];

var bikepath;

function initMap() {
    jQuery.getJSON('/coordwithid_test', function (data) {
        jQuery.each(data, function (index, value) {
            var myCoordinate = {lat: value.lat, lng: value.lng, key: value.key};
            allCoordinates.push(myCoordinate);
        });
    });
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 49.261226, lng: -123.1139271},
        zoom: 12
    });
    var input = document.getElementById('pac-input');
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);
    autocomplete.addListener('place_changed', function() {
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            window.alert("Autocomplete's returned place contains no geometry");
            return;
        } else {
            var LatLng = {lat: place.geometry.location.lat(),lng:place.geometry.location.lng()};
            makeNewMarkerMap(LatLng, place.name);
        }
    });
}

function trackCurrentLocation(){
    if (document.getElementById('currentloc').checked==true){
        if(navigator.geolocation) {
            browserSupportFlag = true;
            navigator.geolocation.getCurrentPosition(function(position) {
                var LatLng = {lat: position.coords.latitude,lng:position.coords.longitude};
                makeNewMarkerMap(LatLng, "Your Current Location");
            }, function() {
                handleNoGeolocation(browserSupportFlag);
            });
        }
        else {
            browserSupportFlag = false;
            handleNoGeolocation(browserSupportFlag);
        }
        function handleNoGeolocation(errorFlag) {
            if (errorFlag == true) {
                alert("Geolocation service failed.");
                initialLocation = vancouver;
            } else {
                alert("Your browser doesn't support geolocation. ");
                initialLocation = vancouver;
            }
            map.setCenter(initialLocation);
        }
    }
}

function makeNewMarkerMap(pos, title){
    markers.forEach(function(marker) {
        marker.setMap(null);
    });
    markers = [];
    markers.push(new google.maps.Marker({
        position: pos,
        map: map,
        title: title
    }));
    map.setCenter(pos);
    map.setZoom(17);
    lastInputtedCoordinate = pos;
}

function makeNewPathMap(bikeRoutes){
    polylines.forEach(function(route) {
        route.setMap(null);
    });
    polylines = [];
    jQuery.each(bikeRoutes, function (index, value) {
        var path = new google.maps.Polyline({
            path: value.coords,
            geodesic: true,
            strokeColor: value.color,
            strokeOpacity: 1.0,
            strokeWeight: 3
        });
        path.setMap(map);
        polylines.push(path);
    });
    map.setZoom(13);
}

function findThreeRoutes() {
    var route0Coordinates = [];
    var route1Coordinates = [];
    var route2Coordinates = [];

    if (lastInputtedCoordinate == null)
        alert("Please set a location!");
    tempAllCoordinates = allCoordinates.slice();

    var r1 = findRoute(route0Coordinates);
    var r2 = findRoute(route1Coordinates);
    var r3 = findRoute(route2Coordinates);

    var p1 = {coords: r1, color: "#FF0000"};
    var p2 = {coords: r2, color: "#FF00FF"};
    var p3 = {coords: r3, color: "#000000"};

    var bikeRoutes = [];
    bikeRoutes.push(p1);
    bikeRoutes.push(p2);
    bikeRoutes.push(p3);

    makeNewPathMap(bikeRoutes);
}

function findRoute(coords){
    var closestPoint = getClosestPoint(lastInputtedCoordinate, tempAllCoordinates);
    filterByKey(closestPoint.key,coords);
    var keyless = removeKey(coords);
    var finalCoords = polylineCoords(keyless);
    return finalCoords;
}

function getClosestPoint(selectedLatLng, points) {
    var closestPoint = null;
    var distance = null;
    var tempDistance = null;

    jQuery.each(points, function(index, value) {
        tempDistance = getDistance(selectedLatLng, value);
        if (distance == null) {
            distance = tempDistance;
            closestPoint = value;
        }
        else if (tempDistance < distance) {
            distance = tempDistance;
            closestPoint = value;
        }
    });
    return closestPoint;
}

function getDistance(p1, p2) {
    //var lat1 = selectedLatLng.lat;
    //var lng1 = selectedLatLng.lng;
    //var lat2 = otherLatLng.lat;
    //var lng2 = otherLatLng.lng;
    //var sidea = Math.abs(lat1 - lat2);
    //var sideb = Math.abs(lng1 - lng2);
    //return (Math.sqrt(sidea*sidea+sideb*sideb));

    //var p1 = new google.maps.LatLng(selectedLatLng.lat, selectedLatLng.lng);
    //var p2 = new google.maps.LatLng(otherLatLng.lat, otherLatLng.lng);
    //d = (google.maps.geometry.spherical.computeDistanceBetween(p1, p2));
    //return d;

    var rad = function(x) {
        return x * Math.PI / 180;
    };

    var r = 6378137;
    var dLat = rad(p2.lat - p1.lat);
    var dLong = rad(p2.lng - p1.lng);
    var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(rad(p1.lat)) * Math.cos(rad(p2.lat)) *
        Math.sin(dLong / 2) * Math.sin(dLong / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    var d = r * c;
    return d;


}

function filterByKey(key, coords) {
    for(var i = 0; i < tempAllCoordinates.length; i++){
        if (tempAllCoordinates[i].key == key){
            coords.push(tempAllCoordinates[i]);
            tempAllCoordinates.splice(i,1);
            i--;
        }
    }

}

function removeKey(coords) {
    var coordsWithoutKey = [];
    jQuery.each(coords, function (index, value) {
        var coordWithoutKey = {lat: value.lat, lng: value.lng};
        coordsWithoutKey.push(coordWithoutKey);
    });
    return coordsWithoutKey;
}

function polylineCoords(coords) {
    var finalCoords = [];
    var startPoint = lastInputtedCoordinate;

    for (var i = 0; i = coords.length; i++) {
        var closestPoint = getClosestPoint(startPoint, coords);
        finalCoords.push(closestPoint);
        for(var j = 0; j < coords.length; j++){
            if(closestPoint == coords[j]){
                coords.splice(j, 1);
                j--;
            }
        }
        startPoint = closestPoint;
        closestPoint = null;
    }

    for (var i = 0; i < finalCoords.length-1; i++) {
        var j = i+1;
        var d = getDistance(finalCoords[i],finalCoords[j]);
        if (d>650){
            finalCoords.splice(j, 1);
            i--;
        }
    }
    return finalCoords;
}

function fetchData() {
    jQuery.getJSON('/coordwithid_test', function (data) {
        alert('Please wait while we fetch data...');
        var coordinates = [];
        jQuery.each(data, function (index, value) {
            var myLatLng = {lat: value.lat, lng: value.lng};
            var marker = new google.maps.Marker
            ({
                position: myLatLng,
                map: map,
                title: JSON.stringify(myLatLng)
            });
            markers.push(marker);
        });
    });
}
