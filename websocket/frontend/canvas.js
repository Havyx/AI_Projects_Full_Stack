(async () => {
  const useFrameRate = 30;
  const stream = await navigator.mediaDevices.getUserMedia ({video: true});
  const capture = new ImageCapture (stream.getVideoTracks ()[0]);
  const socket = new WebSocket ('ws://localhost:3333');
  const options = {imageWidth: 640, imageHeight: 480};
  socket.addEventListener ('open', () => {
    const send = () =>
      capture
        .takePhoto (options)
        .then (blob => socket.send (blob))
        .catch (() => {});
    const sendloop = setInterval (send, 240);
  });
  socket.onmessage = e => {
    console.log (JSON.parse (e.data));
  };
  if (navigator.getUserMedia) {
    navigator.getUserMedia (
      {audio: false, video: {width: 1280, height: 720}},
      function (stream) {
        var video = document.querySelector ('video');
        video.srcObject = stream;
        video.onloadedmetadata = function (e) {
          video.play ();
        };
      },
      function (err) {
        console.log ('The following error occurred: ' + err.name);
      }
    );
  } else {
    console.log ('getUserMedia not supported');
  }
}) ();
