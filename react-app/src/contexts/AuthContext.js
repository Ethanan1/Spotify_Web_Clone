// AuthContext.js
import React, { createContext, useState, useContext, useEffect } from 'react';
import axios from 'axios';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [playlists, setPlaylists] = useState([]);

  const fetchPlaylists = async () => {
    try {
      const response = await axios.get('/api/playlists');
      const fetchedPlaylists = response.data.playlists;
      setPlaylists(fetchedPlaylists);
    } catch (error) {
      console.error(error);
    }
  };


  // Login function
  const login = async (credentials) => {
    try {
      // Make a POST request to your backend /login endpoint
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
      });

      if (response.ok) {
        const user = await response.json();
        setUser(user);
        setIsAuthenticated(true);
        fetchPlaylists(); // Fetch playlists after successful login
      } else {
        const error = await response.json();
        console.error(error);
      }
    } catch (error) {
      console.error(error);
    }
  };

  // Signup function
  const signup = async (formData) => {
    try {
      // Make a POST request to your backend /signup endpoint
      const response = await fetch('/api/auth/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });

      if (response.ok) {
        const user = await response.json();
        setUser(user);
        setIsAuthenticated(true);
        fetchPlaylists(); // Fetch playlists after successful signup
      } else {
        const error = await response.json();
        console.error(error);
      }
    } catch (error) {
      console.error(error);
    }
  };

  // Logout function
  const logout = async () => {
    try {
      // Make a GET request to your backend /logout endpoint
      const response = await fetch('/api/auth/logout');

      if (response.ok) {
        setUser(null);
        setIsAuthenticated(false);
      } else {
        const error = await response.json();
        console.error(error);
      }
    } catch (error) {
      console.error(error);
    }
  };

  // Provide the context values
  const authContextValues = {
    user,
    isAuthenticated,
    playlists,
    login,
    signup,
    logout
  };

  useEffect(() => {
    if (isAuthenticated) {
      fetchPlaylists(); // Fetch playlists when the user is authenticated
    }
  }, [isAuthenticated]);

  return (
    <AuthContext.Provider value={authContextValues}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook to access the AuthContext
export const useAuth = () => useContext(AuthContext); // Export useAuth directly
