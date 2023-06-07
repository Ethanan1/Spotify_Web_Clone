import React, { useContext } from 'react';
import { AuthContext } from '../contexts/AuthContext';

const NavigationModal = () => {
  const { user, logout } = useContext(AuthContext);

  const handleLogout = () => {
    logout();
  };

  return (
    <div>
      <h3>User Info</h3>
      {user && user.email && (
        <p>
          <strong>Email:</strong> {user.email}
        </p>
      )}
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default NavigationModal;
