import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SearchResultsPage = ({ searchQuery }) => {
  const [searchResults, setSearchResults] = useState([]);

  useEffect(() => {
    const fetchSearchResults = async () => {
      try {
        const response = await axios.get(`/api/songs?q=${searchQuery}`);
        const searchResultsData = response.data.songs;
        setSearchResults(searchResultsData);
      } catch (error) {
        console.error('Failed to search for songs:', error);
      }
    };

    fetchSearchResults();
  }, [searchQuery]);

  // Add a song to favorites
  const handleAddToFavorites = async (song) => {
    try {
      await axios.post('/api/favorites', { song_id: song.id });
      // Handle success or update the state accordingly
    } catch (error) {
      console.error('Failed to add song to favorites:', error);
    }
  };

  return (
    <div>
      <h2>Search Results</h2>
      {searchResults.map((song) => (
        <div key={song.id}>
          <h3>{song.title}</h3>
          <p>{song.artist}</p>
          <button onClick={() => handleAddToFavorites(song)}>Add to Favorites</button>
        </div>
      ))}
    </div>
  );
};

export default SearchResultsPage;
