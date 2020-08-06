function getMapData(){
    var newData = {
      "playlist_name":document.getElementById('name').value,
      "origin":document.getElementById('origin-input').value,
      "destination":document.getElementById('destination-input').value
    };

    if(newData["playlist_name"] == '' || 
        newData['origin'] == '' || 
        newData["destination"] == '') 
    {
        document.getElementById('error').innerHTML="Origin, destination, and playlist name cannot be empty";
        return;
    }

    $.getJSON({
          url: "/generate_playlist",
          data: newData,
          success: function(data){
            if(data.is_new_playlist == false){
                document.getElementById('error').innerHTML="Playlist already exists. Enter a new name.";
                document.getElementById('name').value = "";
            }
            document.getElementById("edit_playlist").style.visibility = "visible";
            document.getElementById("playlist").src=data.src;
          }
      });
  }
  
  function removePlaylist(){
    var playlist = {
      "playlist":document.getElementById("playlist").src
    };
    $.getJSON({
      url: "/remove_playlist",
      data: playlist,
      success: function(data){
        document.getElementById("edit_playlist").style.visibility = "hidden";
        document.getElementById("playlist").src="";
      }
  });
  }
  
  function editPlaylist(){
    var url = document.getElementById("playlist").src;
    url = url.replace('embed/', '');
    var win = window.open(url, '_blank');
    win.focus();
  }