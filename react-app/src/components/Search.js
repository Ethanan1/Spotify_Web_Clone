import React, { useState } from 'react';
import axios from 'axios';

const Search = ({ onSearch }) => {
  const [query, setQuery] = useState('');

  const handleSearch = async (e) => {
    e.preventDefault();
    // Perform search request
    try {
      const response = await axios.get(`/api/search?q=${query}`);
      onSearch(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSearch}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search songs and playlists"
        />
        <button type="submit">Search</button>
      </form>
    </div>
  );
};

export default Search;
