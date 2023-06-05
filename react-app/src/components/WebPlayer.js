import React from 'react';
import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';


const WebPlayer = () => {
  return (
    <div>
      <h3>Web Player</h3>
      <AudioPlayer
        src="song_url.mp3"
        autoPlay
        onPlay={() => console.log('onPlay')}
        onPause={() => console.log('onPause')}
        onEnded={() => console.log('onEnded')}
        onError={(e) => console.error(e)}
      />
    </div>
  );
};


export default WebPlayer;
