import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import LoginForm from './components/HomePage/LoginForm';
import SignupForm from './components/HomePage/SignupForm';
import Home from './pages/Home';
import './app.css';

function App() {
  const [showLogin, setShowLogin] = useState(true);

  const handleToggleForm = () => {
    setShowLogin(!showLogin);
  };

  return (
    <Router>
      <div className="container">
        <div className="logo">
          <h1>My Spotify Clone</h1>
        </div>
        <div className="form">
          <Switch>
            <Route exact path="/">
              {showLogin ? <LoginForm /> : <SignupForm />}
              <button onClick={handleToggleForm} className="toggle-button">
                {showLogin ? 'Sign Up' : 'Login'}
              </button>
            </Route>
            <Route path="/home">
              <Home />
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
