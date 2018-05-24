console.log('Session ID: ' + sessionId);
console.log('Token: ' + token);


var session;
var xhttprequest;

var errorMessage = document.querySelector('h1');
var successMessage = document.querySelector('h2');


if(OT.checkSystemRequirements() == 1){
  console.log('This browser supports WebRTC.');
  session = OT.initSession(apiKey, sessionId);

  session.connect(token, function(error) {
    if(error)
      console.log('Cannot connect to the session.');
    else
      console.log('Connected to the session');
  });

  session.on("streamCreated", function(event) {
    session.subscribe(event.stream, 'subscriber',
      {inserMode:'append', width:'50%', height:'50%'}
    );
    console.log('Successfully subscribe');
    successMessage.textContent = 'Live';
    errorMessage.textContent = '';
  });


  session.on("streamDestroyed", function(event) {
    event.preventDefault();
    console.log('Failed to subscribe');
    successMessage.textContent = '';
    errorMessage.textContent = 'No streams are available';
  });
}
else // Failed to launch the livestream.
  console.log('Failed');