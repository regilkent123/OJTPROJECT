console.log('Session ID: ' + sessionId);
console.log('Token: ' + token);

var session, publisher;
var HAS_PUBLISH = false;

if (OT.checkSystemRequirements() == 1) {
  session = OT.initSession(apiKey, sessionId);

  session.connect(token, function(error) {
    // If the connection is successful, initialize a publisher and publish to the session
    if (error) {
      console.log("Cannot connect to the session.");
    }
    else {
      console.log("Connected to the session.");

      publisher = OT.initPublisher('publisher', {insertMode: 'append', width:'50%', height:'50%'});

      start_button = document.getElementById("1");
      stop_button = document.getElementById("2");

      StartPublish(start_button);
      StopPublish(stop_button);

      publisher.on({
        streamCreated: function (event) {
          console.log("Publisher started streaming.");
        },
        streamDestroyed: function (event) {
          console.log("Publisher stopped streaming. Reason: " + event.reason);
        }
      });
    }
  });
}
else {
  alert("You're browser does not support WebRTC");
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
          xhr.onreadystatechange = function() {
            if(this.readyState == 4 && this.status == 200){
              alert(this.responseText);
            }
          }

          xhr.open("GET", "/video/startArchive/", true);
          xhr.send();
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
      session.unpublish(publisher);
      HAS_PUBLISH = false;
      publisher = OT.initPublisher('publisher', {insertMode: 'append'});

      xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200){
          alert(this.responseText);
        }
      }

      xhr.open("GET", "/video/endArchive/", true);
      xhr.send();
    }
    else {
      alert("No streaming occured");
    }
  });
}






/*


var session = OT.initSession(apiKey, sessionId),
    publisher = OT.initPublisher('publisher'),
    // archiveID = null;

session.connect(token, function(error) {
  if (error) {
    console.error('Failed to connect', error);
  } else {
    session.publish(publisher, function(error) {
      if (error) {
        console.error('Failed to publish', error);
      }
    });
  }
});

session.on('streamCreated', function(event) {
  session.subscribe(event.stream, 'subscribers', {
    insertMode: 'append'
  }, function(error) {
    if (error) {
      console.error('Failed to subscribe', error);
    }
  });
});

session.on('archiveStarted', function(event) {
  archiveID = event.id;
  console.log('ARCHIVE STARTED');
  $('.start').hide();
  $('.stop').show();
  disableForm();
});

session.on('archiveStopped', function(event) {
  archiveID = null;
  console.log('ARCHIVE STOPPED');
  $('.start').show();
  $('.stop').hide();
  enableForm();
});

$(document).ready(function() {
  $('.start').click(function(event) {
    var options = $('.archive-options').serialize();
    disableForm();
    $.post('/start', options).fail(enableForm);
  }).show();
  $('.stop').click(function(event){
    $.get('stop/' + archiveID);
  }).hide();
});


function disableForm() {
  $('.archive-options-fields').attr('disabled', 'disabled');
}

function enableForm() {
  $('.archive-options-fields').removeAttr('disabled');
}*/