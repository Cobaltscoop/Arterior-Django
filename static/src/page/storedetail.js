import "../home/style.css";
import "./storedetail.css";

var map = new naver.maps.Map('map', {
    center: position,
    zoom: 18
});

var markerOptions = {
    position: position,
    map: map,
};

var marker = new naver.maps.Marker(markerOptions);