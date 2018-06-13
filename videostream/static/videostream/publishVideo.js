function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

console.log('Session ID: ' + sessionId);
console.log('Token: ' + token);


var session, publisher;
var HAS_PUBLISH = false;
var archive_id = null;

if (OT.checkSystemRequirements() == 1) {
  session = OT.initSession(apiKey, sessionId);
  initPub();

}
else {
  alert("You're browser does not support WebRTC");
}
function initPub() {
  session.connect(token, function(error) {
    if (error) {
      console.log("Cannot connect to the session.");
    }
    else {
      console.log("Connected to the session.");

      var publisherContainer = document.getElementById('live');

      publisher = OT.initPublisher(publisherContainer, {insertMode: "append", width:'500px', height:'500px'});

      start_button = document.getElementById("start");
      stop_button = document.getElementById("stop");
      start_archive = document.getElementById("start_archive");
      stop_archive = document.getElementById("stop_archive");


      StartPublish(start_button);
      StopPublish(stop_button);
      startArchive(start_archive);
      stopArchive(stop_archive);

      session.on({
        streamDestroyed: function (event) {
          event.preventDefault();
          console.log("Reason: " + event.reason);
        }
      })

      publisher.on({
        streamCreated: function (event) {
          console.log("Publisher started streaming.");
        },
        streamDestroyed: function (event) {
          event.preventDefault();
        
          console.log("Publisher stopped streaming. Reason: " + event.reason);

          HAS_PUBLISH = false;
          xhr.onreadystatechange = function() {
            if(this.readyState == 4 && this.status == 200){
              alert(this.responseText);
              archive_id=null;
              // initPub();
            }
          }


        
        }
      });
    }
  });

}
function StartPublish(start_button){
  start_button.addEventListener("click", function(){
    if(!HAS_PUBLISH){
      session.publish(publisher, function(err) {
        if (err) {
          switch (err.name) {
            case "OT_NOT_CONNECTED":
              showMessage("Publishing your video failed. You are not connected to the internet.");
              break;
            case "OT_CREATE_PEER_CONNECTION_FAILED":
              showMessage("Publishing your video failed. This could be due to a restrictive firewall.");
              break;
            default:
              showMessage("An unknown error occurred while trying to publish your video. Please try again later.");
          }
          publisher.destroy();
          publisher = null;
        }
        else {
          console.log(sessionId)
          HAS_PUBLISH = true;
          xhr = new XMLHttpRequest();
          xhr.onreadystatechange = function(e) {
            if(this.readyState == 4 && this.status == 200){
              
              // var response = JSON.parse(this.responseText)
              // archive_id = response.archive_id
              // alert(this.responseText);

            }
          }
          
        }
      });
    }
    else {
        alert("Streaming is on going");
    }
  });
}

function StopPublish(stop_button){
  stop_button.addEventListener("click", function(){
    if(HAS_PUBLISH) {
      session.unpublish(publisher)

    
      xhr.onreadystatechange = function() {
    if(this.readyState == 4 && this.status == 200){
      alert(this.responseText);
      archive_id=null;
      
    }
  }
  console.log("unpublish");
}
    else {
      alert("No streaming occured");
    }
  });
}

// function myFunction() {
//     var confirmation = confirm("Save video to archive?");
//     if (confirmation == true) {
//          console.log("Saved to Archived Videos");
//          StartPublish(start_button);
//     } 
//     else {
//         console.log("Unsaved");{
//         StopPublish(stop_button);
//       }
//     } 
// }

function startArchive(start_archive){
    console.log("archiving starts")
    xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function(e) {
      if(this.readyState == 4 && this.status == 200){
        
        var response = JSON.parse(this.responseText)
        archive_id = response.archive_id
        alert(this.responseText);

      }
    }
    xhr.open("GET", "/video/startArchive/", true);
    xhr.send();
}

function stopArchive(stop_archive){
      
      xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function() {
            if(this.readyState == 4 && this.status == 200){
              alert(this.responseText);
              
              console.log("archiving ends")
            }
          }
      xhr.open("GET", "/video/endArchive/?archive_id=" + archive_id, true);
      xhr.setRequestHeader('X-CSRFToken', getCookie("csrftoken"))
      xhr.send("archive_id=" + archive_id);
}















































// function listArchive(list_archive){
//   list_archive.addEventListener("click", function())_{
//     xhr = new XMLHttpRequest();

    
//       xhr.onreadystatechange = function() {
//         if(this.readyState == 4 && this.status == 200){
//           alert(this.responseText);
//         }
//       }    

//   });
// }