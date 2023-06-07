import React, { useContext } from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import LoginPage from './components/LoginPage';
import SignupPage from './components/SignupPage';
import Dashboard from './components/Dashboard';
import SearchResultsPage from './components/SearchResultsPage';
import { AuthProvider, AuthContext, useAuth } from './contexts/AuthContext';
import './App.css';
// import spotifyLogo from './spotify-logo.png';

const App = () => {
  return (
    <AuthProvider>
      <Router>
        <div className="app-container">
          <div className="app-header">
            <h1 className="app-title">Spotify</h1>
            
          </div>
          <div className="auth-buttons">
            <Link to="/login" className="button">Login</Link>
            <Link to="/signup" className="button">Sign up</Link>
          </div>
          <Switch>
            <Route path="/search-results">
              <SearchResultsPage />
            </Route>
            <Route path="/">
              <AppContent />
            </Route>
          </Switch>
        </div>
      </Router>
    </AuthProvider>
  );
};

const AppContent = () => {
  const { user, isAuthenticated } = useContext(AuthContext);

  return (
    <div className="content-container">
      {isAuthenticated ? (
        <Dashboard user={user} />
      ) : (
        <Switch>
          <Route path="/login" component={LoginPage} />
          <Route path="/signup" component={SignupPage} />
        </Switch>
      )}
    </div>
  );
};

export default App;
