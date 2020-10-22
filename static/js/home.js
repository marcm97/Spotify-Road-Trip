function getMapData(){
    var e = document.getElementById("dropdown");
    var selected_playlist = e.options[e.selectedIndex].text;
    var newData = {
      "origin": document.getElementById('origin-input').value,
      "destination": document.getElementById('destination-input').value,
      "selected_playlist": selected_playlist
    };

    if(newData['selected_playlist'] == "Add to new or existing playlist?")
    {
      document.getElementById('status').innerHTML="Please select a playlist";
      return;
    }

    if( newData['origin'] == '' || 
        newData["destination"] == '') 
    {
        document.getElementById('status').innerHTML="Origin, and destination cannot be empty";
        return;
    }

    $.getJSON({
          url: "/generate_playlist",
          data: newData,
          success: function(data){
            /*document.getElementById('show_playlist').style.display = "block";
            if(data.is_new_playlist == false){
                document.getElementById('playlistStatus').innerHTML= newData["selected_playlist"] + " already exists";
            } else {
                document.getElementById('playlistStatus').innerHTML= newData["selected_playlist"] + " is created";
            }
            
            document.getElementById('playlistInfo').innerHTML="Add playlist info";
            document.getElementById("playlist").src=data.src;*/
            document.getElementById('status').innerHTML = "Songs added \"" + data['playlist']+"\". Enjoy listening! :)"
            location.href = "#generated_playlist";
          }
      });
  }
  
  /*function removePlaylist(){
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
  }*/