function getMapData(){
    var newData = {
      "playlist_name": document.getElementById('name').value,
      "origin": document.getElementById('origin-input').value,
      "destination": document.getElementById('destination-input').value
    };

    if(newData["playlist_name"] == '' || 
        newData['origin'] == '' || 
        newData["destination"] == '') 
    {
        document.getElementById('status').innerHTML="Origin, destination, and playlist name cannot be empty";
        return;
    }

    $.getJSON({
          url: "/generate_playlist",
          data: newData,
          success: function(data){
            document.getElementById('show_playlist').style.display = "block";
            if(data.is_new_playlist == false){
                document.getElementById('playlistStatus').innerHTML= newData["playlist_name"] + " already exists";
            } else {
                document.getElementById('playlistStatus').innerHTML= newData["playlist_name"] + " is created";
            }
            
            document.getElementById('playlistInfo').innerHTML="Add playlist info";
            document.getElementById("playlist").src=data.src;
            location.href = "#generated_playlist";
          }
      });
  }
  
  function removePlaylist(){
    var playlist = {
      "playlist":document.getElementById("playlist").src
    };

    var playlist_name = document.getElementById('name').value;
    $.getJSON({
      url: "/remove_playlist",
      data: playlist,
      success: function(data){
        document.getElementById('status').innerHTML= playlist_name + " is removed";
        document.getElementById("playlist").src="";
        document.getElementById('show_playlist').style.display = "none";
      }
  });
  }
  
  function editPlaylist(){
    var url = document.getElementById("playlist").src;
    url = url.replace('embed/', '');
    var win = window.open(url, '_blank');
    win.focus();
  }