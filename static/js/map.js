// *
// * Add multiple markers
// * 2013 - en.marnoto.com
// *

// necessary variables
var map;
var infoWindow;
var heatmap;
var heatmapdata;

var buildingdata = [
   {
      lat: 42.4498226,
      lng: -76.481841,
      name: "PSB",
      weight: 0.4
   },
   {
      lat: 42.4448765,
      lng: -76.4808143,
      name: "Gates Hall",
      weight: 0.2
   }
];


function initMap() {
   var mapOptions = {
      center: new google.maps.LatLng(40.601203,-8.668173),
      zoom: 9,
      mapTypeId: 'roadmap',
   };

   map = new google.maps.Map(document.getElementById('map'), mapOptions);

   // a new Info Window is created
   infoWindow = new google.maps.InfoWindow();

   // Event that closes the Info Window with a click on the map
   google.maps.event.addListener(map, 'click', function() {
      infoWindow.close();
   });

   // Finally displayMarkers() function is called to begin the markers creation
   displayMarkers();

   heatmap();
}


// This function will iterate over buildingdata array
// creating markers with createMarker function
function displayMarkers(){

   // this variable sets the map bounds according to markers position
   var bounds = new google.maps.LatLngBounds();

   // for loop traverses buildingdata array calling createMarker function for each marker
   for (var i = 0; i < buildingdata.length; i++){

      var latlng = new google.maps.LatLng(buildingdata[i].lat, buildingdata[i].lng);
      var name = buildingdata[i].name;

      createMarker(latlng, name);

      // marker position is added to bounds variable
      bounds.extend(latlng);
   }

   // Finally the bounds variable is used to set the map bounds
   // with fitBounds() function
   map.fitBounds(bounds);
}

// This function creates each marker and it sets their Info Window content
function createMarker(latlng, name){
   var marker = new google.maps.Marker({
      map: map,
      position: latlng,
      title: name
   });

   // This event expects a click on a marker
   // When this event is fired the Info Window content is created
   // and the Info Window is opened.
   google.maps.event.addListener(marker, 'click', function() {
     map.setZoom(18);
     map.setCenter(marker.getPosition());
     binfo.innerHTML = name;
   });
}

function add_to_heatmapdata() {
  heatmapdata=[];
  for (var i = 0; i < buildingdata.length; i++) {
    var latlng = new google.maps.LatLng(buildingdata[i].lat, buildingdata[i].lng);
    heatmapdata.push({location: latlng, weight: buildingdata[i].weight});
  }
}

function heatmap() {
  add_to_heatmapdata();
  heatmap = new google.maps.visualization.HeatmapLayer({
            data: heatmapdata,
            radius: 50
  });
  heatmap.setMap(map);
}
