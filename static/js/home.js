function getMapData(){
    var newData = {
      "playlist_name": document.getElementById('name').value,
      "origin": "Boston, MA, USA",  //document.getElementById('origin-input').value,
      "destination":"New York, NY, USA" //document.getElementById('destination-input').value
    };

    if(newData["playlist_name"] == '' || 
        newData['origin'] == '' || 
        newData["destination"] == '') 
    {
        document.getElementById('tripInfo').innerHTML="Origin, destination, and playlist name cannot be empty";
        return;
    }

    document.getElementById('msg').innerHTML="Creating playlist...";

    $.getJSON({
          url: "/generate_playlist",
          data: newData,
          success: function(data){
            document.getElementById('generated_playlist').style.display = "block";
            if(data.is_new_playlist == false){
                document.getElementById('msg').innerHTML="Playlist already exists. Enter a new name.";
                document.getElementById('name').value = "";
            } else {
                document.getElementById('msg').innerHTML="Playlist created.";
            }
            document.getElementById("playlist").src=data.src;
            location.href = "#first";
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
        document.getElementById('tripInfo').innerHTML="Playlist removed.";
        document.getElementById("playlist").src="";
        document.getElementById('generated_playlist').style.display = "none";
      }
  });
  }
  
  function editPlaylist(){
    var url = document.getElementById("playlist").src;
    url = url.replace('embed/', '');
    var win = window.open(url, '_blank');
    win.focus();
  }