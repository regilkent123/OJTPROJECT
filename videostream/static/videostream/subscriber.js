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
    var subscriberContainer = document.getElementById('topnav');
    session.subscribe(event.stream, subscriberContainer,
      {insertMode:'replace', width:'100%', height:'100%'}
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
else 
  console.log('Failed');
