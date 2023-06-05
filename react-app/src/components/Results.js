import React from 'react';

const Results = ({ results }) => {
  return (
    <div>
      <h3>Search Results</h3>
      <ul>
        {results.map((result) => (
          <li key={result.id}>{result.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default Results;
