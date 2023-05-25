import React, { useState } from 'react';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';
import './components/login.css';

function App() {
  const [showLogin, setShowLogin] = useState(true);

  const handleToggleForm = () => {
    setShowLogin(!showLogin);
  };

  return (
    <div className="container">
      <div className="logo">
        <h1>My Spotify Clone</h1>
      </div>
      <div className="form">
        {showLogin ? <LoginForm /> : <SignupForm />}
        <button onClick={handleToggleForm} className="toggle-button">
          {showLogin ? 'Sign Up' : 'Login'}
        </button>
      </div>
    </div>
  );
}

export default App;
