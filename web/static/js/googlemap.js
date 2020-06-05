function initAutocomplete() {
    let mapDiv = document.getElementById('mapdiv');
    map = new google.maps.Map(mapDiv, {
        center: {
            lat: 49.2827,
            lng: -123.1207
        },
        zoom: 13,
        mapTypeId: 'roadmap'
    });

    // Create the search box and link it to the UI element.
    var input = document.getElementById('gmap-input');
    var searchBox = new google.maps.places.SearchBox(input);

    // This moves the input box onto the map. Commented out in case we want to use it later.
    // map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

    // Bias the SearchBox results towards current map's viewport.
    map.addListener('bounds_changed', function() {
        searchBox.setBounds(map.getBounds());
    });

    var markers = [];
    // Listen for the event fired when the user selects a prediction and retrieve
    // more details for that place.
    searchBox.addListener('places_changed', function() {
        var places = searchBox.getPlaces();

        if (places.length == 0) {
            return;
        }

        // Clear out the old markers.
        markers.forEach(function(marker) {
            marker.setMap(null);
        });
        markers = [];

        // For each place, get the icon, name and location.
        var bounds = new google.maps.LatLngBounds();
        places.forEach(function(place) {
            console.log(place);
            if (!place.geometry) {
                console.log("Returned place contains no geometry ");
                return;
            }
            callPlusCodesApi(place.geometry.location)
            var icon = {
                url: place.icon,
                size: new google.maps.Size(71, 71),
                origin: new google.maps.Point(0, 0),
                anchor: new google.maps.Point(17, 34),
                scaledSize: new google.maps.Size(25, 25)
            };

            // Create a marker for each place.
            markers.push(new google.maps.Marker({
                map: map,
                title: place.name,
                position: place.geometry.location
            }));

            if (place.geometry.viewport) {
                // Only geocodes have viewport.
                bounds.union(place.geometry.viewport);
            } else {
                bounds.extend(place.geometry.location);
            }
        });
        map.fitBounds(bounds);
    });
}

function callPlusCodesApi(bounds) {
    // TODO: THIS IS BASICALLY CALLBACK HELL BUT W/ PROMISES
    fetch(`https://plus.codes/api?address=${bounds.lat()},${bounds.lng()}&ekey=AIzaSyCocZZTCz9pr5gtn5Yx69pG-h4zdwtMBU4&language=en`)
    .then(res => res.json())
    .then(json => {
        let plus_code = json.plus_code.global_code;
        updatePlusCode(plus_code);
        // TODO: extract into function
        fetch(`${baseUrl}/lookup_olc?olc=${plus_code}`)
        .then(res => res.json())
        .then(json => {
          updateWordPhrase(json.phrase)
        })
    })
        .catch(err => console.error(err));
}
