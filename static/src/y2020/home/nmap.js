// 지도의 중심위치 계산하기
var map = new naver.maps.Map(document.getElementById('naver-map'), {
	center: new naver.maps.LatLng(CENTER[0], CENTER[1]),
	zoom: 14,
});
  
// 지도에 표시할 var Marker 객체 생성
var markers = [],
	infoWindows = [];
for (const [popup, latlng] of Object.entries(POSITIONS)) {
	var slugtext = latlng[2]
	var marker = new naver.maps.Marker({
		position: new naver.maps.LatLng(latlng[0], latlng[1]),
		map: map,
		// title: popup,
		icon: {
			url: markerImg,
			size: new naver.maps.Size(24, 37),
			anchor: new naver.maps.Point(12, 37),
		},
		zIndex: 100
	});
	
	var infoWindow = new naver.maps.InfoWindow({
			content: '<div class="naver-marker"><a href="/store/' + slugtext + '">'+ popup +'</a></div>'
	});
	markers.push(marker);
	infoWindows.push(infoWindow);
}
  
function updateMarkers(map, markers) {
	var mapBounds = map.getBounds();
	var marker, position;
	for (var i = 0; i < markers.length; i++) {
		marker = markers[i]
		position = marker.getPosition();
		if (mapBounds.hasLatLng(position)) {
			showMarker(map, marker);
		} else {
			hideMarker(map, marker);
		}
	}
}
  
function showMarker(map, marker) {
	if (marker.setMap()) return;
	marker.setMap(map);
}
  
function hideMarker(map, marker) {
	if (!marker.setMap()) return;
	marker.setMap(null);
}
  
// 해당 마커의 인덱스를 seq라는 클로저 변수로 저장하는 이벤트 핸들러를 반환합니다.
function getClickHandler(seq) {
	return function(e) {
		var marker = markers[seq],
			infoWindow = infoWindows[seq];
		if (infoWindow.getMap()) {
			infoWindow.close();
		} else {
			infoWindow.open(map, marker);
		}
	}
}
  
for (var i=0, ii=markers.length; i<ii; i++) {
	naver.maps.Event.addListener(markers[i], 'click', getClickHandler(i));
}

// 최초 지도생성시 실행 이벤트
naver.maps.Event.addListener(map, 'idle', function() {
	updateMarkers(map, markers);
});