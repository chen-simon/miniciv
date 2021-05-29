const startGame = async () => {
    playerName = document.getElementById("data").value;
    center = map.getCenter();
    lat = center.lat();
    lng = center.lng();
    zoom = map.getZoom();

    await fetch('/start/', {method: 'POST', body: JSON.stringify({'playername': playerName, 'lat': lat, 'lng': lng, 'zoom': zoom})});
};