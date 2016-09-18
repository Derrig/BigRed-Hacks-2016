$.getScript('{{url_for('static', filename='heatMapData')}}',function())
{
  function initMap() {
    var heatMapData;
    var map;
    var heatmap;
    map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: 42.4472051, lng: -76.48297680000002},
      zoom: 15
    });
    heatmap = new google.maps.visualization.HeatmapLayer({
              data: dataList
              radius: 50
    });
    heatmap.setMap(map);
  }
}
