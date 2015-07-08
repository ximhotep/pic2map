var LocationMap = {
  'initialize': function initialize() {
    // Map centered in NowSecure HQ by default
    this.map = L.map('map').setView([40.2001925,-89.0876265], 3);
    this.markerCluster = L.markerClusterGroup();

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(this.map);
    this.map.addLayer(this.markerCluster);
  },
  'addMarkers': function addMarkers(markersData) {
    console.log('Adding ' + markersData.length + ' markers');
    markersData.forEach(function(markerData) {
        var marker = L.marker([markerData.latitude, markerData.longitude]);
        var text = 'Filename: ' + markerData.filename;
        if (markerData.datetime) {
          text += '<br>GPS datetime: ' + markerData.datetime;
        }

        marker.bindPopup(text);
        this.markerCluster.addLayer(marker);
    }, this);
  }
};