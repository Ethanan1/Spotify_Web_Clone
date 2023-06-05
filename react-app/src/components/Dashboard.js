import React, { useState } from 'react';
import Search from './Search';
import Results from './Results';
import WebPlayer from './WebPlayer';

const Dashboard = () => {
  const [searchResults, setSearchResults] = useState([]);

  const handleSearch = (results) => {
    setSearchResults(results);
  };

  return (
    <div>
      <h2>Dashboard</h2>
      <Search onSearch={handleSearch} />
      <Results results={searchResults} />
      <WebPlayer />
    </div>
  );
};

export default Dashboard;
