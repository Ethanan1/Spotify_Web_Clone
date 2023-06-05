import React from 'react';
import LoginPage from './components/LoginPage';
import SignupPage from './components/SignupPage';

const App = () => {
  return (
    <div>
      <h1>Welcome to My App</h1>
      <LoginPage />
      <SignupPage />
      {/* Add other components and routes here */}
    </div>
  );
};

export default App;
